//
//  Networking.swift
//  Servisync
//
//  Created by Dmitrii Gorovoi on 10.11.2024.
//

import Foundation
import UIKit
import SwiftUI
import CoreLocation


func uploadData(
    image: UIImage,
    location: CLLocationCoordinate2D,
    completion: @escaping (Result<Data, Error>) -> Void
) {
    guard let url = URL(string: "http://10.87.0.190:5000/process") else {
        print("Invalid server URL")
        return
    }
    
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    
    // Convert the image to JPEG data
    guard let imageData = image.jpegData(compressionQuality: 0.8) else {
        print("Failed to convert image to JPEG data")
        return
    }
        
    
    guard let imageData = image.jpegData(compressionQuality: 0.8) else {
        print("Failed to convert image to JPEG data")
        return
    }
    let base64ImageString = imageData.base64EncodedString()
    
    // Create the JSON payload
    let payload: [String: Any] = [
        "image": base64ImageString,
        "location": [
            "latitude": location.latitude,
            "longitude": location.longitude
        ]
    ]
    
    print("created payload")
    do {
        let jsonData = try JSONSerialization.data(withJSONObject: payload, options: [])
        request.httpBody = jsonData
        
        let session = URLSession.shared
        session.dataTask(with: request) { responseData, _, error in
            if let error = error {
                completion(.failure(error))
            } else if let responseData = responseData {
                completion(.success(responseData))
                print("Completed")
            }
        }.resume()
    } catch {
        completion(.failure(error))
    }
}

func uploadEditedData(
    status: Status,
    address: String,
    location_in_building: String,
    completion: @escaping (Result<Void, Error>) -> Void
) {
    guard let url = URL(string: "http://10.87.0.190:5000/submit") else {
        print("Invalid server URL")
        return
    }
    let locationManager = LocationManager.shared
    
    guard let location = locationManager.location else {
        print("location not available")
        return
    }
    
    // Combine all parameters into one object
    let combinedData = CombinedData(
        age: status.age,
        equipment_name: status.equipment_name,
        equipment_type: status.equipment_type,
        manufacturer: status.manufacturer,
        model: status.model,
        serial_number: status.serial_number,
        size: status.size,
        material: status.type_of_material,
        additional_data: status.additional_data,
        building_address: address,
        location_in_building: location_in_building,
        location_longitude: location.longitude,
        location_latitude: location.latitude
    )
    
    print(location.latitude, location.longitude)
    
    print(combinedData)
    
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    do {
        // Encode the combined object
        let jsonData = try JSONEncoder().encode(combinedData)
        request.httpBody = jsonData

        let session = URLSession.shared
        session.dataTask(with: request) { _, _, error in
            if let error = error {
                completion(.failure(error))
            } else {
                completion(.success(()))
                print("Updated")
            }
        }.resume()
    } catch {
        completion(.failure(error))
    }
}
struct CombinedData: Codable {
    var age: String?
    var equipment_name: String?
    var equipment_type: String?
    var manufacturer: String?
    var model: String?
    var serial_number: String?
    var size: String?
    var material: String?
    var additional_data: [String: String]?
    var building_address: String
    var location_in_building: String
    var location_longitude: CLLocationDegrees
    var location_latitude: CLLocationDegrees
}


class EntryViewModel: ObservableObject {
    static let shared = EntryViewModel()
    
    @Published var entries: [Entry] = []
    
    private init() {}
    
    func fetchEntries() {
        guard let url = URL(string: "http://10.87.0.190:5000/getentries") else {
            print("Invalid URL")
            return
        }
        
        URLSession.shared.dataTask(with: url) { data, response, error in
            if let error = error {
                print("Error fetching data: \(error)")
                return
            }
            
            guard let data = data else {
                print("No data returned")
                return
            }
            
            do {
                let decodedEntries = try JSONDecoder().decode([Entry].self, from: data)
                DispatchQueue.main.async {
                    self.entries = decodedEntries
                }
            } catch {
                print("Error decoding JSON: \(error)")
            }
        }.resume()
    }
}
