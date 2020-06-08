//
//  ViewController.swift
//  LocustApp
//
//  Created by Sohil Bhatia on 6/6/20.
//  Copyright © 2020 Sohil Bhatia. All rights reserved.
//

import UIKit
import FirebaseDatabase
import CoreLocation

class ViewController: UIViewController, CLLocationManagerDelegate {
var locationManager = CLLocationManager()
var ref: DatabaseReference!
    
    @IBOutlet weak var phoneField: UITextField!
    @IBOutlet weak var nameField: UITextField!
    @IBOutlet weak var nameText: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        ref = Database.database().reference()
        // Do any additional setup after loading the vie
        nameField.textColor = UIColor.white
        phoneField.textColor = UIColor.white
  
        locationManager = CLLocationManager()
        locationManager.requestAlwaysAuthorization()
        locationManager.startUpdatingLocation()
        locationManager.delegate = self

    }
   func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
       if let location = locations.last {
           ref?.child("Latitude").setValue(Float(location.coordinate.latitude))
           ref?.child("Longitude").setValue(Float(location.coordinate.longitude))
       }
   }
    
    

    @IBAction func buttonClicked(_ sender: Any) {
        ref?.child("Phone Number").setValue(phoneField.text!)
        ref?.child("Name").setValue(nameField.text!)
        let url = URL(string: "http://localhost:7071/api/Tracker?name=Sohil")!

        let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
            guard let data = data else { return }
            print(String(data: data, encoding: .utf8)!)
        }
        task.resume()
    }
    
}


