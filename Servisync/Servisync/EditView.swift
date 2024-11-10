//
//  EditView.swift
//  Servisync
//
//  Created by Dmitrii Gorovoi on 10.11.2024.
//

import SwiftUI


struct EditView: View {
    @Binding var status: Status
    @State private var address: String?
    @State private var location_in_building: String = ""
    @StateObject private var viewModel = EntryViewModel.shared
    @Environment(\.presentationMode) var presentationMode
    
    init(status: Binding<Status>, location: String) {
        _status = status
        _address = State(initialValue: location)
    }
    
    var body: some View {
        VStack {
            Form {
//                TextField("Equipment Name", text: Binding($status.equipment_name, default: ""))
//                TextField("Age", text: Binding($status.age, default: ""))
//                TextField("Equipment Type", text: Binding($status.equipment_type, default: ""))
//                TextField("Manufacturer", text: Binding($status.manufacturer, default: ""))
//                TextField("Model", text: Binding($status.model, default: ""))
//                TextField("Serial Number", text: Binding($status.serial_number, default: ""))
//                TextField("Size", text: Binding($status.size, default: ""))
//                TextField("Type of Material", text: Binding($status.type_of_material, default: ""))
//                TextField("Address", text: Binding($address, default: ""))
//                TextField("Location in building", text: $location_in_building)
            Section(header: Text("Equipment Details")) {
                            VStack(alignment: .leading) {
                                Text("Equipment Name")
                                    .font(.subheadline)
                                    .foregroundColor(.gray)
                                TextField("Enter equipment name", text: Binding($status.equipment_name, default: ""))
                                    .textFieldStyle(RoundedBorderTextFieldStyle())
                                    .padding(.bottom)
                            }

                            VStack(alignment: .leading) {
                                Text("Equipment Type")
                                    .font(.subheadline)
                                    .foregroundColor(.gray)
                                TextField("Enter equipment type", text: Binding($status.equipment_type, default: ""))
                                    .textFieldStyle(RoundedBorderTextFieldStyle())
                                    .padding(.bottom)
                            }
                                
                            VStack(alignment: .leading) {
                                Text("Equipment Size")
                                    .font(.subheadline)
                                    .foregroundColor(.gray)
                                TextField("Enter equipment size", text: Binding($status.size, default: ""))
                                    .textFieldStyle(RoundedBorderTextFieldStyle())
                                    .padding(.bottom)
                            }

                
                            VStack(alignment: .leading) {
                                Text("Manufacturer")
                                    .font(.subheadline)
                                    .foregroundColor(.gray)
                                TextField("Enter manufacturer", text: Binding($status.manufacturer, default: ""))
                                    .textFieldStyle(RoundedBorderTextFieldStyle())
                                    .padding(.bottom)
                            }

                            VStack(alignment: .leading) {
                                Text("Model")
                                    .font(.subheadline)
                                    .foregroundColor(.gray)
                                TextField("Enter model", text: Binding($status.model, default: ""))
                                    .textFieldStyle(RoundedBorderTextFieldStyle())
                                    .padding(.bottom)
                            }

                            VStack(alignment: .leading) {
                                Text("Serial Number")
                                    .font(.subheadline)
                                    .foregroundColor(.gray)
                                TextField("Enter serial number", text: Binding($status.serial_number, default: ""))
                                    .textFieldStyle(RoundedBorderTextFieldStyle())
                                    .padding(.bottom)
                            }

                            VStack(alignment: .leading) {
                                Text("Material")
                                    .font(.subheadline)
                                    .foregroundColor(.gray)
                                TextField("Enter material", text: Binding($status.type_of_material, default: ""))
                                    .textFieldStyle(RoundedBorderTextFieldStyle())
                                    .padding(.bottom)
                            }

                            VStack(alignment: .leading) {
                                Text("Age")
                                    .font(.subheadline)
                                    .foregroundColor(.gray)
                                TextField("Enter age", text: Binding($status.age, default: ""))
                                    .textFieldStyle(RoundedBorderTextFieldStyle())
                                    .padding(.bottom)
                            }
                        }

                Section(header: Text("Location Details")) {
                    VStack(alignment: .leading) {
                        Text("Location")
                            .font(.subheadline)
                            .foregroundColor(.gray)
                        TextField("Enter location", text: Binding($address, default: ""))
                            .textFieldStyle(RoundedBorderTextFieldStyle())
                            .padding(.bottom)
                    }
                    
                    VStack(alignment: .leading) {
                        Text("Floor")
                            .font(.subheadline)
                            .foregroundColor(.gray)
                        TextField("Enter floor", text: $location_in_building)
                            .textFieldStyle(RoundedBorderTextFieldStyle())
                            .padding(.bottom)
                    }
                    
                    
                    Button("Submit") {
                        // Handle submission
                        submitEditedData()
                        presentationMode.wrappedValue.dismiss()
                    }
                }
            }
        }
    }

    func submitEditedData() {
        // Example function to handle data submission
        uploadEditedData(status: status, address: address ?? "", location_in_building: location_in_building) { result in
            switch result {
            case .success:
                print("Data submitted successfully")
                viewModel.fetchEntries()
            case .failure(let error):
                print("Submission error: \(error)")
            }
        }
    }
}

extension Binding {
    init(_ source: Binding<Value?>, default defaultValue: Value) {
        self.init(
            get: { source.wrappedValue ?? defaultValue },
            set: { source.wrappedValue = $0 }
        )
    }
}
