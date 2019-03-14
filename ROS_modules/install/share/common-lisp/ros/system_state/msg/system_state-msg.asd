
(cl:in-package :asdf)

(defsystem "system_state-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ButtonPress" :depends-on ("_package_ButtonPress"))
    (:file "_package_ButtonPress" :depends-on ("_package"))
  ))