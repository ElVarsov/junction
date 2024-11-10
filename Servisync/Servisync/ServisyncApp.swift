//
//  ServisyncApp.swift
//  Servisync
//
//  Created by Dmitrii Gorovoi on 10.11.2024.
//

import SwiftUI

@main
struct ServisyncApp: App {
    let persistenceController = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
