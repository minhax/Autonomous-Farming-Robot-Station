
(cl:in-package :asdf)

(defsystem "custom_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "PlantBox" :depends-on ("_package_PlantBox"))
    (:file "_package_PlantBox" :depends-on ("_package"))
    (:file "SerialRequest" :depends-on ("_package_SerialRequest"))
    (:file "_package_SerialRequest" :depends-on ("_package"))
  ))