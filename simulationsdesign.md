Simulation eines Sprints

Zielgröße:
* Abarbeitungsstand (%) zum Sprintende (Timebox),
* Dauer bis zur kompletten Abarbeitung aller User Storys

Jeweils ein Batch von N User Storys pro Sprint , jeweils mit Aufwand x , der 
normalverteilt ist mit mü = T-Shirt-Schätzung, sigma als freier Parameter. Die 
Verteilung der T-Shirtgrößen pro Sprint ist bekannt. Die User Storys bilden ein DAG, 
das die Abhängigkeitsstruktur abbildet. Jeder Arbeiter hat einen Wert für Skill-Level, 
der aus einer Zufallsvariable mit Normalverteilung (0, tau) gezogen wird. 
Der Skill-Level zeigt, um wieviel % der Arbeiter eine Aufgabe schneller oder langsamer 
als der Durchschnitt erledigt.

Gesetzte Parameter im ersten Ansatz:
* Dauer der Timebox
* N : Anzahl User Storys, d.h. Batchgröße, Sprint Backlog Größe
* M : Anzahl Arbeiter
* Einfaches DAG, jede User Story kann einzeln bearbeitet werden 

Parameter der Experimente im ersten Ansatz:
* sigma: Standardabweichung der normalverteilten Variable für die Schätzgenauigkeit des Aufwands
* tau: Standardabweichung der normalverteilten Variable für den Skill-Level der Arbeiter

Annahme:
* kein Bias in den Schätzungen für Aufwand, d.h. die Schätzung ist der Erwartungswert, ist der Mittelwert
* kein Bias in der Skill-Level Verteilung, d.h. das Feature Team besitzt keine systematisch schlechten Leute

