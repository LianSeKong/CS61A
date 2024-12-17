(define (square n) (* n n))

(define (pow base exp) 
  (cond 
    ((= exp 1) base)
    ((= exp 2) (square base))
    ((even? (modulo exp 2)) (square (pow base (quotient exp 2))))
    (else (* base (square (pow base (quotient exp 2)))))
  )
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y)
      )
  )
)

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ascending? s) 
  (cond 
    ((or (null? s) (null? (cdr s))) #t)
    ((> (car s) (cadr s)) #f)
    (else (ascending? (cdr s)))
  )
)

(define (my-filter pred s)
  (cond 
    ((null? s) s)
    ((pred (car s)) 
      (cons (car s) (my-filter pred (cdr s)))
    )
    (else (my-filter pred (cdr s)))
  )
)

(define (no-repeats s) 
  (cond
    ((null? s) s)
    ((null? (cdr s)) s)
    (else (cons (car s) (no-repeats (my-filter (lambda (x) (not (= x (car s)))) (cdr s)))))
  )
)

; helper function
; returns the values of lst that are bigger than x
; e.g., (larger-values 3 '(1 2 3 4 5 1 2 3 4 5)) --> (4 5 4 5)
(define (larger-values x lst)
  (cond 
    ((null? lst) lst)
    ((< x (car lst)) (cons (car lst) (larger-values x (cdr lst))))
    (else (larger-values x (cdr lst)))
  )
)

(define (longest-increasing-subsequence lst)
  (if (null? lst)
      nil
      (begin (define first (car lst))
             (define rest (cdr lst))
             (define large-values-rest
                    (larger-values first rest)
             )
             (define with-first
                (cons first (longest-increasing-subsequence large-values-rest)
                )
             )
             (define without-first
                  (longest-increasing-subsequence rest)
              )
            (if (> (length with-first) (length without-first))
                 with-first
                 without-first
            )
      )
  )
)



(define (sqrt x)
  (define (good-enough? guess)
    (< (abs (- (square guess) x)) 0.001))
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (good-enough? guess)
        guess
        (sqrt-iter (improve guess))))
  (sqrt-iter 1.0))
(sqrt 9)