(define (over-or-under num1 num2) 
      (cond ((= num1 num2) 0)
            ((< num1 num2) -1)
            ((> num1 num2) 1)
      )
)
(define (make-adder num) (lambda (incr) (+ num incr)))

(define (composed f g) (lambda (x) (f (g x))))

(define (repeat f n) (lambda (x) (if (= n 0) x ((repeat f (- n 1)) (f x)))))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) (if (= 0 (modulo (max a b) (min a b))) (min a b) (gcd (min a b) (modulo (max a b) (min a b)))))

(define (duplicate lst) 
  (if (null? lst)
    lst
    (cons (car lst)
          (cons (car lst) 
                (duplicate (cdr lst))
          )
    )
  )
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (deep-map fn s) 
    (cond ((null? s) s) 
          ((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s)))) 
          (else (cons (fn (car s)) (deep-map fn (cdr s)))) 
))
