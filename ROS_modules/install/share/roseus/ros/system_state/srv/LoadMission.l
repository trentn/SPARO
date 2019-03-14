;; Auto-generated. Do not edit!


(when (boundp 'system_state::LoadMission)
  (if (not (find-package "SYSTEM_STATE"))
    (make-package "SYSTEM_STATE"))
  (shadow 'LoadMission (find-package "SYSTEM_STATE")))
(unless (find-package "SYSTEM_STATE::LOADMISSION")
  (make-package "SYSTEM_STATE::LOADMISSION"))
(unless (find-package "SYSTEM_STATE::LOADMISSIONREQUEST")
  (make-package "SYSTEM_STATE::LOADMISSIONREQUEST"))
(unless (find-package "SYSTEM_STATE::LOADMISSIONRESPONSE")
  (make-package "SYSTEM_STATE::LOADMISSIONRESPONSE"))

(in-package "ROS")





(defclass system_state::LoadMissionRequest
  :super ros::object
  :slots ())

(defmethod system_state::LoadMissionRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass system_state::LoadMissionResponse
  :super ros::object
  :slots (_json_mission ))

(defmethod system_state::LoadMissionResponse
  (:init
   (&key
    ((:json_mission __json_mission) "")
    )
   (send-super :init)
   (setq _json_mission (string __json_mission))
   self)
  (:json_mission
   (&optional __json_mission)
   (if __json_mission (setq _json_mission __json_mission)) _json_mission)
  (:serialization-length
   ()
   (+
    ;; string _json_mission
    4 (length _json_mission)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _json_mission
       (write-long (length _json_mission) s) (princ _json_mission s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _json_mission
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _json_mission (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass system_state::LoadMission
  :super ros::object
  :slots ())

(setf (get system_state::LoadMission :md5sum-) "cf76547124a8eccb32585a0d744f179b")
(setf (get system_state::LoadMission :datatype-) "system_state/LoadMission")
(setf (get system_state::LoadMission :request) system_state::LoadMissionRequest)
(setf (get system_state::LoadMission :response) system_state::LoadMissionResponse)

(defmethod system_state::LoadMissionRequest
  (:response () (instance system_state::LoadMissionResponse :init)))

(setf (get system_state::LoadMissionRequest :md5sum-) "cf76547124a8eccb32585a0d744f179b")
(setf (get system_state::LoadMissionRequest :datatype-) "system_state/LoadMissionRequest")
(setf (get system_state::LoadMissionRequest :definition-)
      "---
string json_mission
")

(setf (get system_state::LoadMissionResponse :md5sum-) "cf76547124a8eccb32585a0d744f179b")
(setf (get system_state::LoadMissionResponse :datatype-) "system_state/LoadMissionResponse")
(setf (get system_state::LoadMissionResponse :definition-)
      "---
string json_mission
")



(provide :system_state/LoadMission "cf76547124a8eccb32585a0d744f179b")


