;; Auto-generated. Do not edit!


(when (boundp 'custom_msgs::PlantBox)
  (if (not (find-package "CUSTOM_MSGS"))
    (make-package "CUSTOM_MSGS"))
  (shadow 'PlantBox (find-package "CUSTOM_MSGS")))
(unless (find-package "CUSTOM_MSGS::PLANTBOX")
  (make-package "CUSTOM_MSGS::PLANTBOX"))

(in-package "ROS")
;;//! \htmlinclude PlantBox.msg.html


(defclass custom_msgs::PlantBox
  :super ros::object
  :slots (_x _y _length _width ))

(defmethod custom_msgs::PlantBox
  (:init
   (&key
    ((:x __x) 0)
    ((:y __y) 0)
    ((:length __length) 0)
    ((:width __width) 0)
    )
   (send-super :init)
   (setq _x (round __x))
   (setq _y (round __y))
   (setq _length (round __length))
   (setq _width (round __width))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:length
   (&optional __length)
   (if __length (setq _length __length)) _length)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:serialization-length
   ()
   (+
    ;; uint32 _x
    4
    ;; uint32 _y
    4
    ;; uint32 _length
    4
    ;; uint32 _width
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _x
       (write-long _x s)
     ;; uint32 _y
       (write-long _y s)
     ;; uint32 _length
       (write-long _length s)
     ;; uint32 _width
       (write-long _width s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _x
     (setq _x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _y
     (setq _y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _length
     (setq _length (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _width
     (setq _width (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get custom_msgs::PlantBox :md5sum-) "2c2b959d705840bcab8520e8edc01dee")
(setf (get custom_msgs::PlantBox :datatype-) "custom_msgs/PlantBox")
(setf (get custom_msgs::PlantBox :definition-)
      "uint32 x
uint32 y
uint32 length
uint32 width

")



(provide :custom_msgs/PlantBox "2c2b959d705840bcab8520e8edc01dee")


