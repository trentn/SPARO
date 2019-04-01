; Auto-generated. Do not edit!


(cl:in-package system_state-srv)


;//! \htmlinclude DetectTarget-request.msg.html

(cl:defclass <DetectTarget-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass DetectTarget-request (<DetectTarget-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectTarget-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectTarget-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name system_state-srv:<DetectTarget-request> is deprecated: use system_state-srv:DetectTarget-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectTarget-request>) ostream)
  "Serializes a message object of type '<DetectTarget-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectTarget-request>) istream)
  "Deserializes a message object of type '<DetectTarget-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectTarget-request>)))
  "Returns string type for a service object of type '<DetectTarget-request>"
  "system_state/DetectTargetRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectTarget-request)))
  "Returns string type for a service object of type 'DetectTarget-request"
  "system_state/DetectTargetRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectTarget-request>)))
  "Returns md5sum for a message object of type '<DetectTarget-request>"
  "771f4495ccebaf28e2e698ac883f1d20")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectTarget-request)))
  "Returns md5sum for a message object of type 'DetectTarget-request"
  "771f4495ccebaf28e2e698ac883f1d20")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectTarget-request>)))
  "Returns full string definition for message of type '<DetectTarget-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectTarget-request)))
  "Returns full string definition for message of type 'DetectTarget-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectTarget-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectTarget-request>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectTarget-request
))
;//! \htmlinclude DetectTarget-response.msg.html

(cl:defclass <DetectTarget-response> (roslisp-msg-protocol:ros-message)
  ((json_state
    :reader json_state
    :initarg :json_state
    :type cl:string
    :initform "")
   (X
    :reader X
    :initarg :X
    :type cl:integer
    :initform 0)
   (Y
    :reader Y
    :initarg :Y
    :type cl:integer
    :initform 0)
   (Z
    :reader Z
    :initarg :Z
    :type cl:integer
    :initform 0))
)

(cl:defclass DetectTarget-response (<DetectTarget-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectTarget-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectTarget-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name system_state-srv:<DetectTarget-response> is deprecated: use system_state-srv:DetectTarget-response instead.")))

(cl:ensure-generic-function 'json_state-val :lambda-list '(m))
(cl:defmethod json_state-val ((m <DetectTarget-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader system_state-srv:json_state-val is deprecated.  Use system_state-srv:json_state instead.")
  (json_state m))

(cl:ensure-generic-function 'X-val :lambda-list '(m))
(cl:defmethod X-val ((m <DetectTarget-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader system_state-srv:X-val is deprecated.  Use system_state-srv:X instead.")
  (X m))

(cl:ensure-generic-function 'Y-val :lambda-list '(m))
(cl:defmethod Y-val ((m <DetectTarget-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader system_state-srv:Y-val is deprecated.  Use system_state-srv:Y instead.")
  (Y m))

(cl:ensure-generic-function 'Z-val :lambda-list '(m))
(cl:defmethod Z-val ((m <DetectTarget-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader system_state-srv:Z-val is deprecated.  Use system_state-srv:Z instead.")
  (Z m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectTarget-response>) ostream)
  "Serializes a message object of type '<DetectTarget-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'json_state))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'json_state))
  (cl:let* ((signed (cl:slot-value msg 'X)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'Y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'Z)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectTarget-response>) istream)
  "Deserializes a message object of type '<DetectTarget-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'json_state) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'json_state) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'X) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'Y) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'Z) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectTarget-response>)))
  "Returns string type for a service object of type '<DetectTarget-response>"
  "system_state/DetectTargetResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectTarget-response)))
  "Returns string type for a service object of type 'DetectTarget-response"
  "system_state/DetectTargetResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectTarget-response>)))
  "Returns md5sum for a message object of type '<DetectTarget-response>"
  "771f4495ccebaf28e2e698ac883f1d20")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectTarget-response)))
  "Returns md5sum for a message object of type 'DetectTarget-response"
  "771f4495ccebaf28e2e698ac883f1d20")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectTarget-response>)))
  "Returns full string definition for message of type '<DetectTarget-response>"
  (cl:format cl:nil "string json_state~%int64 X~%int64 Y~%int64 Z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectTarget-response)))
  "Returns full string definition for message of type 'DetectTarget-response"
  (cl:format cl:nil "string json_state~%int64 X~%int64 Y~%int64 Z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectTarget-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'json_state))
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectTarget-response>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectTarget-response
    (cl:cons ':json_state (json_state msg))
    (cl:cons ':X (X msg))
    (cl:cons ':Y (Y msg))
    (cl:cons ':Z (Z msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'DetectTarget)))
  'DetectTarget-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'DetectTarget)))
  'DetectTarget-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectTarget)))
  "Returns string type for a service object of type '<DetectTarget>"
  "system_state/DetectTarget")