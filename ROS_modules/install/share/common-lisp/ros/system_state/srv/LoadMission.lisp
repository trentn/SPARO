; Auto-generated. Do not edit!


(cl:in-package system_state-srv)


;//! \htmlinclude LoadMission-request.msg.html

(cl:defclass <LoadMission-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass LoadMission-request (<LoadMission-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LoadMission-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LoadMission-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name system_state-srv:<LoadMission-request> is deprecated: use system_state-srv:LoadMission-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LoadMission-request>) ostream)
  "Serializes a message object of type '<LoadMission-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LoadMission-request>) istream)
  "Deserializes a message object of type '<LoadMission-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LoadMission-request>)))
  "Returns string type for a service object of type '<LoadMission-request>"
  "system_state/LoadMissionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LoadMission-request)))
  "Returns string type for a service object of type 'LoadMission-request"
  "system_state/LoadMissionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LoadMission-request>)))
  "Returns md5sum for a message object of type '<LoadMission-request>"
  "cf76547124a8eccb32585a0d744f179b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LoadMission-request)))
  "Returns md5sum for a message object of type 'LoadMission-request"
  "cf76547124a8eccb32585a0d744f179b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LoadMission-request>)))
  "Returns full string definition for message of type '<LoadMission-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LoadMission-request)))
  "Returns full string definition for message of type 'LoadMission-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LoadMission-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LoadMission-request>))
  "Converts a ROS message object to a list"
  (cl:list 'LoadMission-request
))
;//! \htmlinclude LoadMission-response.msg.html

(cl:defclass <LoadMission-response> (roslisp-msg-protocol:ros-message)
  ((json_mission
    :reader json_mission
    :initarg :json_mission
    :type cl:string
    :initform ""))
)

(cl:defclass LoadMission-response (<LoadMission-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LoadMission-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LoadMission-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name system_state-srv:<LoadMission-response> is deprecated: use system_state-srv:LoadMission-response instead.")))

(cl:ensure-generic-function 'json_mission-val :lambda-list '(m))
(cl:defmethod json_mission-val ((m <LoadMission-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader system_state-srv:json_mission-val is deprecated.  Use system_state-srv:json_mission instead.")
  (json_mission m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LoadMission-response>) ostream)
  "Serializes a message object of type '<LoadMission-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'json_mission))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'json_mission))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LoadMission-response>) istream)
  "Deserializes a message object of type '<LoadMission-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'json_mission) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'json_mission) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LoadMission-response>)))
  "Returns string type for a service object of type '<LoadMission-response>"
  "system_state/LoadMissionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LoadMission-response)))
  "Returns string type for a service object of type 'LoadMission-response"
  "system_state/LoadMissionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LoadMission-response>)))
  "Returns md5sum for a message object of type '<LoadMission-response>"
  "cf76547124a8eccb32585a0d744f179b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LoadMission-response)))
  "Returns md5sum for a message object of type 'LoadMission-response"
  "cf76547124a8eccb32585a0d744f179b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LoadMission-response>)))
  "Returns full string definition for message of type '<LoadMission-response>"
  (cl:format cl:nil "string json_mission~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LoadMission-response)))
  "Returns full string definition for message of type 'LoadMission-response"
  (cl:format cl:nil "string json_mission~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LoadMission-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'json_mission))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LoadMission-response>))
  "Converts a ROS message object to a list"
  (cl:list 'LoadMission-response
    (cl:cons ':json_mission (json_mission msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'LoadMission)))
  'LoadMission-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'LoadMission)))
  'LoadMission-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LoadMission)))
  "Returns string type for a service object of type '<LoadMission>"
  "system_state/LoadMission")