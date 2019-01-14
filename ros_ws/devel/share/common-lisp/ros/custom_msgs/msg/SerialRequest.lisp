; Auto-generated. Do not edit!


(cl:in-package custom_msgs-msg)


;//! \htmlinclude SerialRequest.msg.html

(cl:defclass <SerialRequest> (roslisp-msg-protocol:ros-message)
  ((Code
    :reader Code
    :initarg :Code
    :type cl:fixnum
    :initform 0)
   (Length
    :reader Length
    :initarg :Length
    :type cl:fixnum
    :initform 0)
   (Buffer
    :reader Buffer
    :initarg :Buffer
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 64 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass SerialRequest (<SerialRequest>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SerialRequest>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SerialRequest)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_msgs-msg:<SerialRequest> is deprecated: use custom_msgs-msg:SerialRequest instead.")))

(cl:ensure-generic-function 'Code-val :lambda-list '(m))
(cl:defmethod Code-val ((m <SerialRequest>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:Code-val is deprecated.  Use custom_msgs-msg:Code instead.")
  (Code m))

(cl:ensure-generic-function 'Length-val :lambda-list '(m))
(cl:defmethod Length-val ((m <SerialRequest>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:Length-val is deprecated.  Use custom_msgs-msg:Length instead.")
  (Length m))

(cl:ensure-generic-function 'Buffer-val :lambda-list '(m))
(cl:defmethod Buffer-val ((m <SerialRequest>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msgs-msg:Buffer-val is deprecated.  Use custom_msgs-msg:Buffer instead.")
  (Buffer m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SerialRequest>) ostream)
  "Serializes a message object of type '<SerialRequest>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Code)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'Code)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Length)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'Length)) ostream)
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream))
   (cl:slot-value msg 'Buffer))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SerialRequest>) istream)
  "Deserializes a message object of type '<SerialRequest>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Code)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'Code)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Length)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'Length)) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'Buffer) (cl:make-array 64))
  (cl:let ((vals (cl:slot-value msg 'Buffer)))
    (cl:dotimes (i 64)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SerialRequest>)))
  "Returns string type for a message object of type '<SerialRequest>"
  "custom_msgs/SerialRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SerialRequest)))
  "Returns string type for a message object of type 'SerialRequest"
  "custom_msgs/SerialRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SerialRequest>)))
  "Returns md5sum for a message object of type '<SerialRequest>"
  "c3caf2e11f9a4e075e8eb559468402d7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SerialRequest)))
  "Returns md5sum for a message object of type 'SerialRequest"
  "c3caf2e11f9a4e075e8eb559468402d7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SerialRequest>)))
  "Returns full string definition for message of type '<SerialRequest>"
  (cl:format cl:nil "uint16 Code~%uint16 Length~%uint8[64] Buffer~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SerialRequest)))
  "Returns full string definition for message of type 'SerialRequest"
  (cl:format cl:nil "uint16 Code~%uint16 Length~%uint8[64] Buffer~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SerialRequest>))
  (cl:+ 0
     2
     2
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'Buffer) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SerialRequest>))
  "Converts a ROS message object to a list"
  (cl:list 'SerialRequest
    (cl:cons ':Code (Code msg))
    (cl:cons ':Length (Length msg))
    (cl:cons ':Buffer (Buffer msg))
))
