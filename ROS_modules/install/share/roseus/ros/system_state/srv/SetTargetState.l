;; Auto-generated. Do not edit!


(when (boundp 'system_state::SetTargetState)
  (if (not (find-package "SYSTEM_STATE"))
    (make-package "SYSTEM_STATE"))
  (shadow 'SetTargetState (find-package "SYSTEM_STATE")))
(unless (find-package "SYSTEM_STATE::SETTARGETSTATE")
  (make-package "SYSTEM_STATE::SETTARGETSTATE"))
(unless (find-package "SYSTEM_STATE::SETTARGETSTATEREQUEST")
  (make-package "SYSTEM_STATE::SETTARGETSTATEREQUEST"))
(unless (find-package "SYSTEM_STATE::SETTARGETSTATERESPONSE")
  (make-package "SYSTEM_STATE::SETTARGETSTATERESPONSE"))

(in-package "ROS")





(defclass system_state::SetTargetStateRequest
  :super ros::object
  :slots (_json_desiredstate ))

(defmethod system_state::SetTargetStateRequest
  (:init
   (&key
    ((:json_desiredstate __json_desiredstate) "")
    )
   (send-super :init)
   (setq _json_desiredstate (string __json_desiredstate))
   self)
  (:json_desiredstate
   (&optional __json_desiredstate)
   (if __json_desiredstate (setq _json_desiredstate __json_desiredstate)) _json_desiredstate)
  (:serialization-length
   ()
   (+
    ;; string _json_desiredstate
    4 (length _json_desiredstate)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _json_desiredstate
       (write-long (length _json_desiredstate) s) (princ _json_desiredstate s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _json_desiredstate
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _json_desiredstate (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass system_state::SetTargetStateResponse
  :super ros::object
  :slots (_state_reached ))

(defmethod system_state::SetTargetStateResponse
  (:init
   (&key
    ((:state_reached __state_reached) 0)
    )
   (send-super :init)
   (setq _state_reached (round __state_reached))
   self)
  (:state_reached
   (&optional __state_reached)
   (if __state_reached (setq _state_reached __state_reached)) _state_reached)
  (:serialization-length
   ()
   (+
    ;; int8 _state_reached
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _state_reached
       (write-byte _state_reached s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _state_reached
     (setq _state_reached (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _state_reached 127) (setq _state_reached (- _state_reached 256)))
   ;;
   self)
  )

(defclass system_state::SetTargetState
  :super ros::object
  :slots ())

(setf (get system_state::SetTargetState :md5sum-) "e48ef780cf73cc26b8047ad6ac36082b")
(setf (get system_state::SetTargetState :datatype-) "system_state/SetTargetState")
(setf (get system_state::SetTargetState :request) system_state::SetTargetStateRequest)
(setf (get system_state::SetTargetState :response) system_state::SetTargetStateResponse)

(defmethod system_state::SetTargetStateRequest
  (:response () (instance system_state::SetTargetStateResponse :init)))

(setf (get system_state::SetTargetStateRequest :md5sum-) "e48ef780cf73cc26b8047ad6ac36082b")
(setf (get system_state::SetTargetStateRequest :datatype-) "system_state/SetTargetStateRequest")
(setf (get system_state::SetTargetStateRequest :definition-)
      "string json_desiredstate
---
int8 state_reached
")

(setf (get system_state::SetTargetStateResponse :md5sum-) "e48ef780cf73cc26b8047ad6ac36082b")
(setf (get system_state::SetTargetStateResponse :datatype-) "system_state/SetTargetStateResponse")
(setf (get system_state::SetTargetStateResponse :definition-)
      "string json_desiredstate
---
int8 state_reached
")



(provide :system_state/SetTargetState "e48ef780cf73cc26b8047ad6ac36082b")


