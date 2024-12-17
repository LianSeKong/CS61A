(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values)
  (cons keys (cons values nil))
)

(define (get-keys-kwlist1 kwlist) (car kwlist))

(define (get-values-kwlist1 kwlist)
  (cadr kwlist)
)

(define (make-kwlist2 keys values)
  (if (null? keys) 
    nil 
    (cons (cons 
            (car keys) 
            (cons (car values) 
                  nil
            )
          ) 
          (make-kwlist2 
            (cdr keys)
            (cdr values)
          )
    )
  ) 
)

(define (get-keys-kwlist2 kwlist) 
  (if (null? kwlist) nil (cons (car (car kwlist)) (get-keys-kwlist2 (cdr kwlist))))
)

(define (get-values-kwlist2 kwlist)
  (if (null? kwlist) nil (cons (cadr (car kwlist)) (get-values-kwlist2 (cdr kwlist))))
)

(define (add-to-kwlist kwlist key value)
  (make-kwlist (append (get-keys-kwlist kwlist) (list key))  (append (get-values-kwlist kwlist) (list value)))
  
)

(define (get-first-from-kwlist kwlist key)
 (let
      (
        (values (get-values-kwlist kwlist))
        (keys (get-keys-kwlist kwlist))
        (find (lambda (f ks vs) 
                      (cond ((null? ks) nil) 
                            ((equal? (car ks) key) (car vs))
                            (else (f 
                                    f
                                    (cdr ks)
                                    (cdr vs)
                                  )
                            )
                      )
              )
        )
      )
      (find find keys values)
  )      
)


