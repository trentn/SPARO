
(cl:in-package :asdf)

(defsystem "system_state-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "DetectTarget" :depends-on ("_package_DetectTarget"))
    (:file "_package_DetectTarget" :depends-on ("_package"))
    (:file "LoadMission" :depends-on ("_package_LoadMission"))
    (:file "_package_LoadMission" :depends-on ("_package"))
    (:file "MoveEndEffector" :depends-on ("_package_MoveEndEffector"))
    (:file "_package_MoveEndEffector" :depends-on ("_package"))
    (:file "MoveRobot" :depends-on ("_package_MoveRobot"))
    (:file "_package_MoveRobot" :depends-on ("_package"))
    (:file "SetTargetState" :depends-on ("_package_SetTargetState"))
    (:file "_package_SetTargetState" :depends-on ("_package"))
  ))