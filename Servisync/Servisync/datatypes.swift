import Foundation

// Fixed structure for the entire response
struct ParsedResponse: Codable {
    var status: Status  // Change 'let' to 'var' to make 'status' mutable
    let location: String
}


// Fixed structure for the status, with additional_data as a dictionary of strings
struct Status: Codable {
    var age: String?
    var equipment_name: String?
    var equipment_type: String?
    var manufacturer: String?
    var model: String?
    var serial_number: String?
    var size: String?
    var type_of_material: String?
    var additional_data: [String: String]?
}


