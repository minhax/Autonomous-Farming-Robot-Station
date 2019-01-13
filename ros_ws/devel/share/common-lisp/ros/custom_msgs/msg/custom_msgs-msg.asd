
(cl:in-package :asdf)

(defsystem "custom_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "PlantBox" :depends-on ("_package_PlantBox"))
    (:file "_package_PlantBox" :depends-on ("_package"))
    (:file "SerialPacket" :depends-on ("_package_SerialPacket"))
    (:file "_package_SerialPacket" :depends-on ("_package"))
  ))