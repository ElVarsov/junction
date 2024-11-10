//
//  ServerResponse.swift
//  Servisync
//
//  Created by Dmitrii Gorovoi on 10.11.2024.
//

import Foundation

struct ServerResponse: Codable {
    var id: Int
    var name: String
    var description: String
    // Add more fields as per your server's response
}
