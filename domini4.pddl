(define (domain domini)

(:requirements :adl :typing)
(:types exercici dia dificultat)
(:functions
  (tempsEx ?ex - exercici)
  (tempsTotal))
(:predicates
  ;(es_exercici ?ex - exercici)
  ;(es_dia ?dia - dia)
  ;(es_dificultat ?dif - dificultat)
  (precursor ?prec - exercici ?ex - exercici)
  (preparador ?prep - exercici ?ex - exercici)
  (esta_fent ?ex - exercici ?dia - dia)
  (esta_fent_dif ?ex - exercici ?dia - dia  ?dif - dificultat) ;s'esta fent un exercici en un dia i amb una dificultat

  (es_ultim ?ex - exercici ?dia - dia)

  (dificultat_actual ?ex - exercici ?dif - dificultat)
  (dia_actual ?dia - dia)

  (es_anterior ?exA - exercici ?exD - exercici ?dia - dia) ;l'exercici exA es fa just abans de exD al dia dia

  (es_dia_posterior ?diaP - dia ?diaA - dia)
  (es_dificultat_posterior ?difP - dificultat ?difA - dificultat)

)

  ;Accions

  (:action seguent-dia
    :parameters (?diaA - dia ?diaP - dia)
    :precondition (and (dia_actual ?diaA)
                  (es_dia_posterior ?diaP ?diaA)
    )
    :effect (and (not (dia_actual ?diaA))
                 (dia_actual ?diaP)
                  (decrease (tempsTotal) (tempsTotal))
    )
  )


  (:action assigna-exercici
          :parameters(?ex - exercici ?dia - dia)
          :precondition (and (<=(+(tempsTotal)(tempsEx ?ex))90)
                          (not(esta_fent ?ex ?dia))
                           (dia_actual ?dia)

                             (or (exists (?exPC - exercici) (and (precursor ?exPC ?ex)(es_ultim ?exPC ?dia)))
                                 (not (exists (?exPC - exercici) (precursor ?exPC ?ex))))
                                 (or (forall (?exP - exercici) (imply (preparador ?exP ?ex)(esta_fent ?exP ?dia)))
                                     (not (exists (?exP - exercici) (preparador ?exP ?ex)))
                                 )
                             )

          :effect(and (forall (?exU - exercici)(when(es_ultim ?exU ?dia) (not(es_ultim ?exU ?dia))))
                      (es_ultim ?ex ?dia)
                      (esta_fent ?ex ?dia)
                      (increase(tempsTotal)(tempsEx ?ex))
            )
  )

  (:action assigna-exercici-dificultat
          :parameters(?ex - exercici ?dif - dificultat ?dia - dia)
          :precondition (and  (<=(+(tempsTotal)(tempsEx ?ex))90)
                              (not(esta_fent ?ex ?dia))
                               (dia_actual ?dia)

                             (or (exists (?exPC - exercici) (and (precursor ?exPC ?ex)(es_ultim ?exPC ?dia)))
                                 (not (exists (?exPC - exercici) (precursor ?exPC ?ex))))
                                 (or (forall (?exP - exercici) (imply (preparador ?exP ?ex)(esta_fent ?exP ?dia)))
                                     (not (exists (?exP - exercici) (preparador ?exP ?ex))))
                             (exists (?difA - dificultat)(and (dificultat_actual ?ex ?difA) (es_dificultat_posterior ?dif ?difA)))

                             )

          :effect(and (forall (?exU - exercici)(when(es_ultim ?exU ?dia) (not(es_ultim ?exU ?dia))))
                      (es_ultim ?ex ?dia)

                      (forall (?difA - dificultat)
                                           (when (dificultat_actual ?ex ?difA)(not (dificultat_actual ?ex ?difA))))
                     (dificultat_actual ?ex ?dif)
                     (esta_fent ?ex ?dia)
                     (increase(tempsTotal)(tempsEx ?ex))
            )
  )



)
