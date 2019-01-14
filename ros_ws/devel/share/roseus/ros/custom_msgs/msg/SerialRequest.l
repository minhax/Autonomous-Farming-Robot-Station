;; Auto-generated. Do not edit!


(when (boundp 'custom_msgs::SerialRequest)
  (if (not (find-package "CUSTOM_MSGS"))
    (make-package "CUSTOM_MSGS"))
  (shadow 'SerialRequest (find-package "CUSTOM_MSGS")))
(unless (find-package "CUSTOM_MSGS::SERIALREQUEST")
  (make-package "CUSTOM_MSGS::SERIALREQUEST"))

(in-package "ROS")
;;//! \htmlinclude SerialRequest.msg.html


(defclass custom_msgs::SerialRequest
  :super ros::object
  :slots (_Code _Length _Buffer ))

(defmethod custom_msgs::SerialRequest
  (:init
   (&key
    ((:Code __Code) 0)
    ((:Length __Length) 0)
    ((:Buffer __Buffer) (make-array 64 :initial-element 0 :element-type :char))
    )
   (send-super :init)
   (setq _Code (round __Code))
   (setq _Length (round __Length))
   (setq _Buffer __Buffer)
   self)
  (:Code
   (&optional __Code)
   (if __Code (setq _Code __Code)) _Code)
  (:Length
   (&optional __Length)
   (if __Length (setq _Length __Length)) _Length)
  (:Buffer
   (&optional __Buffer)
   (if __Buffer (setq _Buffer __Buffer)) _Buffer)
  (:serialization-length
   ()
   (+
    ;; uint16 _Code
    2
    ;; uint16 _Length
    2
    ;; uint8[64] _Buffer
    (* 1    64)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _Code
       (write-word _Code s)
     ;; uint16 _Length
       (write-word _Length s)
     ;; uint8[64] _Buffer
     (princ _Buffer s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _Code
     (setq _Code (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _Length
     (setq _Length (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint8[64] _Buffer
   (setq _Buffer (make-array 64 :element-type :char))
   (replace _Buffer buf :start2 ptr-) (incf ptr- 64)
   ;;
   self)
  )

(setf (get custom_msgs::SerialRequest :md5sum-) "c3caf2e11f9a4e075e8eb559468402d7")
(setf (get custom_msgs::SerialRequest :datatype-) "custom_msgs/SerialRequest")
(setf (get custom_msgs::SerialRequest :definition-)
      "uint16 Code
uint16 Length
uint8[64] Buffer

")



(provide :custom_msgs/SerialRequest "c3caf2e11f9a4e075e8eb559468402d7")


