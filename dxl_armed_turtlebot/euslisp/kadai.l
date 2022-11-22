(dotimes (i 6)

  (setq angle-vector (float-vector 0 0 0 0 0 0))
  (send *dxl-armed-turtlebot* :angle-vector angle-vector)
  (send *ri* :angle-vector angle-vector 3000)
  (send *ri* :wait-interpolation)
  (setf (elt angle-vector i) 60) ;; i 番目の関節のみ 60deg
  (send *ri* :angle-vector angle-vector 3000)
  (send *dxl-armed-turtlebot* :angle-vector angle-vector)
  (send *ri* :wait-interpolation)
  (print "Please press Enter to continue.")
  (read-line) ;; Enter キーを押すのを待つ
  )
