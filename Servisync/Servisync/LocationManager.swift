//
//  LocationManager.swift
//  Servisync
//
//  Created by Dmitrii Gorovoi on 10.11.2024.
//

import Foundation
import CoreLocation

class LocationManager: NSObject, ObservableObject, CLLocationManagerDelegate {
    static let shared = LocationManager()
    
    private let locationManager = CLLocationManager()
    @Published var location: CLLocationCoordinate2D?

    private override init() {
        super.init()
        locationManager.delegate = self
        locationManager.requestWhenInUseAuthorization()
        locationManager.startUpdatingLocation()
    }

    func locationManager(
        _ manager: CLLocationManager,
        didUpdateLocations locations: [CLLocation]
    ) {
        guard let latestLocation = locations.last else { return }

        // Check if the location accuracy is within an acceptable range
        if latestLocation.horizontalAccuracy < 100 { // Adjust this value as needed
            location = latestLocation.coordinate
            locationManager.stopUpdatingLocation() // Stop updates when an accurate location is obtained
        }
    }


    func locationManager(
        _ manager: CLLocationManager,
        didFailWithError error: Error
    ) {
        print("Error getting location: \(error)")
    }
}

