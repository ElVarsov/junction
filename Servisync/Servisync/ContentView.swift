//
//  ContentView.swift
//  Servisync
//
//  Created by Dmitrii Gorovoi on 10.11.2024.
//

import SwiftUI
import UIKit
import CoreData


struct ContentView: View {
    @State private var showingImagePicker = false
    @State private var inputImage: UIImage?
    @State private var showEditView = false
    @StateObject private var locationManager = LocationManager.shared
    // Update the type of serverResponse to ParsedResponse?
    @StateObject private var responseModel = ServerResponseModel()
    @StateObject private var viewModel = EntryViewModel.shared
    
    @State var floor: String? = ""



    var body: some View {
        NavigationView {
            ZStack {
                VStack {
                    Text("Servisync")
                        .multilineTextAlignment(.leading)
                        .padding()
                        .font(.largeTitle)
                        .fontWeight(.bold)
                    
                    HStack {
                        Text("Last entries")
                            .font(.title2)
                            .fontWeight(.semibold)
                            .padding(.bottom, 5)
                        
                        Spacer()
                    }
                    .padding()
                    
                    List(viewModel.entries) { entry in
                        NavigationLink(destination: DetailView(entry: entry)) {
                            HStack {
                                if (entry.equipment_name ?? "") != "" && (entry.equipment_name ?? "") != "Unnamed Equipment" && (entry.equipment_name ?? "") != "N/A" && (entry.equipment_name ?? "") != "None" {
                                    Text(entry.equipment_name ?? "Unnamed Equipment")
                                        .font(.headline)
                                        .frame(maxWidth: .infinity, alignment: .leading)
                                }
                            }
                        }
                    }
                    
                    Button(action: {
                        showingImagePicker = true
                    }) {
                        Text("Scan")
                            .font(.title2) // Customize the font
                            .foregroundColor(.white) // Text color
                            .fontWeight(.semibold)
                            .padding()
                            .frame(maxWidth: .infinity)
                            .background(Color.blue) // Background color
                            .cornerRadius(10) // Rounded corners
                    }
                    .padding()
                }
            }
        }
        .sheet(isPresented: $showingImagePicker) {
            ImagePicker(image: $inputImage, sendData: sendData)
        }
        .fullScreenCover(isPresented: $showEditView) {
            if let serverResponse = responseModel.serverResponse {
                EditView(status: Binding(
                    get: { serverResponse.status },
                    set: { self.responseModel.serverResponse?.status = $0 }
                ), location: serverResponse.location)
            } else {
                Text("Error: No data available")
            }
        }
        .onAppear{
            viewModel.fetchEntries()
        }

    }
    
    func sendData() {
        guard let image = inputImage,
              let location = locationManager.location else {
            print("Image or location not available")
            return
        }

        uploadData(image: image, location: location) { result in
            switch result {
            case .success(let data):
                parseResponseData(data)
            case .failure(let error):
                print("Upload error: \(error)")
            }
        }
    }
    
    func parseResponseData(_ data: Data) {
        let decoder = JSONDecoder()
        do {
            // Attempt to decode the data into a ParsedResponse object
            let parsedResponse = try decoder.decode(ParsedResponse.self, from: data)
            print("Parsed response: \(parsedResponse)") // Debug print
            
            
            // Perform UI updates on the main thread
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
                self.responseModel.serverResponse = parsedResponse
                self.showEditView = true
            }
        } catch {
            // Print the error if decoding fails
            print("JSON parsing error: \(error)")
        }
    }

}

struct DetailView: View {
    let entry: Entry

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            Text("Equipment Name: \(entry.equipment_name ?? "N/A")")
                .font(.title2)
                .padding(.bottom, 5)
                .fontWeight(.bold)
            
            Text("Equipment Type: \(entry.equipment_type ?? "N/A")")
            Text("Manufacturer: \(entry.manufacturer ?? "N/A")")
            Text("Model: \(entry.model ?? "N/A")")
            Text("Serial Number: \(entry.serial_number ?? "N/A")")
            Text("Material: \(entry.material ?? "N/A")")
            Text("Age: \(entry.age != nil ? "\(entry.age!)" : "N/A")")
            Text("Size: \(entry.size_of_machine ?? "N/A")")
            Text("Location in Building: \(entry.location_in_building ?? "N/A")")
            Text("Building Address: \(entry.building_address ?? "N/A")")
            Text("Additional Data: \(entry.additional_data ?? "N/A")")
            Text("Upload Time: \(entry.upload_time ?? "N/A")")
            
            Spacer()
        }
        .padding()
        .navigationTitle("Details")
        .navigationBarTitleDisplayMode(.inline)
    }
}

struct ImagePicker: UIViewControllerRepresentable {
    @Environment(\.presentationMode) var presentationMode
    @Binding var image: UIImage?
    var sendData: () -> Void

    class Coordinator: NSObject, UINavigationControllerDelegate, UIImagePickerControllerDelegate {
        let parent: ImagePicker

        init(_ parent: ImagePicker) {
            self.parent = parent
        }

        func imagePickerController(
            _ picker: UIImagePickerController,
            didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey: Any]
        ) {
            if let uiImage = info[.originalImage] as? UIImage {
                parent.image = uiImage
                parent.sendData()
            }
            
            parent.presentationMode.wrappedValue.dismiss()
        }

        func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
            parent.presentationMode.wrappedValue.dismiss()
        }
    }

    func makeCoordinator() -> Coordinator { Coordinator(self) }

    func makeUIViewController(context: Context) -> UIImagePickerController {
        let picker = UIImagePickerController()
        picker.delegate = context.coordinator

        if UIImagePickerController.isSourceTypeAvailable(.camera) {
            picker.sourceType = .camera
        } else {
            picker.sourceType = .photoLibrary
        }

        return picker
    }

    func updateUIViewController(_ uiViewController: UIImagePickerController, context: Context) {}
}


private let itemFormatter: DateFormatter = {
    let formatter = DateFormatter()
    formatter.dateStyle = .short
    formatter.timeStyle = .medium
    return formatter
}()

#Preview {
    ContentView().environment(\.managedObjectContext, PersistenceController.preview.container.viewContext)
}

class ServerResponseModel: ObservableObject {
    @Published var serverResponse: ParsedResponse?
}

struct Entry: Codable, Identifiable {
    let id: Int?
    let additional_data: String?
    let age: Int?
    let building_address: String?
    let equipment_model: String?
    let equipment_name: String?
    let equipment_type: String?
    let location_in_building: String?
    let manufacturer: String?
    let material: String?
    let model: String?
    let serial_number: String?
    let size_of_machine: String?
    let upload_time: String?
}

