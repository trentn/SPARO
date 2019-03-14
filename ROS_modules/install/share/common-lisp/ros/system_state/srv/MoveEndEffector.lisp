; Auto-generated. Do not edit!


(cl:in-package system_state-srv)


;//! \htmlinclude MoveEndEffector-request.msg.html

(cl:defclass <MoveEndEffector-request> (roslisp-msg-protocol:ros-message)
  ((X
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

(cl:defclass MoveEndEffector-request (<MoveEndEffector-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveEndEffector-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveEndEffector-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name system_state-srv:<MoveEndEffector-request> is deprecated: use system_state-srv:MoveEndEffector-request instead.")))

(cl:ensure-generic-function 'X-val :lambda-list '(m))
(cl:defmethod X-val ((m <MoveEndEffector-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader system_state-srv:X-val is deprecated.  Use system_state-srv:X instead.")
  (X m))

(cl:ensure-generic-function 'Y-val :lambda-list '(m))
(cl:defmethod Y-val ((m <MoveEndEffector-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader system_state-srv:Y-val is deprecated.  Use system_state-srv:Y instead.")
  (Y m))

(cl:ensure-generic-function 'Z-val :lambda-list '(m))
(cl:defmethod Z-val ((m <MoveEndEffector-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader system_state-srv:Z-val is deprecated.  Use system_state-srv:Z instead.")
  (Z m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveEndEffector-request>) ostream)
  "Serializes a message object of type '<MoveEndEffector-request>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveEndEffector-request>) istream)
  "Deserializes a message object of type '<MoveEndEffector-request>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveEndEffector-request>)))
  "Returns string type for a service object of type '<MoveEndEffector-request>"
  "system_state/MoveEndEffectorRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveEndEffector-request)))
  "Returns string type for a service object of type 'MoveEndEffector-request"
  "system_state/MoveEndEffectorRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveEndEffector-request>)))
  "Returns md5sum for a message object of type '<MoveEndEffector-request>"
  "515108492c7d4ad3a4f126e6820b3140")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveEndEffector-request)))
  "Returns md5sum for a message object of type 'MoveEndEffector-request"
  "515108492c7d4ad3a4f126e6820b3140")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveEndEffector-request>)))
  "Returns full string definition for message of type '<MoveEndEffector-request>"
  (cl:format cl:nil "int64 X~%int64 Y~%int64 Z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveEndEffector-request)))
  "Returns full string definition for message of type 'MoveEndEffector-request"
  (cl:format cl:nil "int64 X~%int64 Y~%int64 Z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveEndEffector-request>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveEndEffector-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveEndEffector-request
    (cl:cons ':X (X msg))
    (cl:cons ':Y (Y msg))
    (cl:cons ':Z (Z msg))
))
;//! \htmlinclude MoveEndEffector-response.msg.html

(cl:defclass <MoveEndEffector-response> (roslisp-msg-protocol:ros-message)
  ((reached_position
    :reader reached_position
    :initarg :reached_position
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass MoveEndEffector-response (<MoveEndEffector-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveEndEffector-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveEndEffector-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name system_state-srv:<MoveEndEffector-response> is deprecated: use system_state-srv:MoveEndEffector-response instead.")))

(cl:ensure-generic-function 'reached_position-val :lambda-list '(m))
(cl:defmethod reached_position-val ((m <MoveEndEffector-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader system_state-srv:reached_position-val is deprecated.  Use system_state-srv:reached_position instead.")
  (reached_position m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveEndEffector-response>) ostream)
  "Serializes a message object of type '<MoveEndEffector-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'reached_position) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveEndEffector-response>) istream)
  "Deserializes a message object of type '<MoveEndEffector-response>"
    (cl:setf (cl:slot-value msg 'reached_position) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveEndEffector-response>)))
  "Returns string type for a service object of type '<MoveEndEffector-response>"
  "system_state/MoveEndEffectorResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveEndEffector-response)))
  "Returns string type for a service object of type 'MoveEndEffector-response"
  "system_state/MoveEndEffectorResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveEndEffector-response>)))
  "Returns md5sum for a message object of type '<MoveEndEffector-response>"
  "515108492c7d4ad3a4f126e6820b3140")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveEndEffector-response)))
  "Returns md5sum for a message object of type 'MoveEndEffector-response"
  "515108492c7d4ad3a4f126e6820b3140")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveEndEffector-response>)))
  "Returns full string definition for message of type '<MoveEndEffector-response>"
  (cl:format cl:nil "bool reached_position~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveEndEffector-response)))
  "Returns full string definition for message of type 'MoveEndEffector-response"
  (cl:format cl:nil "bool reached_position~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveEndEffector-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveEndEffector-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveEndEffector-response
    (cl:cons ':reached_position (reached_position msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MoveEndEffector)))
  'MoveEndEffector-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MoveEndEffector)))
  'MoveEndEffector-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveEndEffector)))
  "Returns string type for a service object of type '<MoveEndEffector>"
  "system_state/MoveEndEffector")