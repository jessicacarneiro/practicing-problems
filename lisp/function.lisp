(defvar a 1)
(defun foo (foo) (print (+ foo foo)))

(foo 3)
(foo 7)
(foo 45)
(foo a)