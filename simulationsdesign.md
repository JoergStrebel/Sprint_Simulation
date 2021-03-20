# Simulations-basiertes Modell
## Design 
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

## Bewertung
Der o.g. Simulationsansatz ist nicht realistisch durchführbar, da ich als Auftraggeber eben nicht weiß,
wie viele Arbeiter tatsächlich vom Dienstleister eingesetzt werden.

# Statistisches Modell 1
Um mit weniger Annahmen auszukommen, betrachten wir hier ein statistisches Modell, mit dem das Risiko der 
Zeitüberschreitung ermittelt werden soll.
## Design
Folgende Größen lassen sich zuverlässig ermitteln oder schätzen:
* Summe der geplanten Story Points pro Sprint X. Dies entspricht der angenommenen Kapazität des Teams pro Sprint K.
* Summe der tatsächlich fertiggestellten Story Points pro Sprint Y.
* Summe der tatsächlichen Überlauf-Story Points pro Sprint Z

Es gilt X=Z+Y.

Folgende Größen lassen sich nur indirekt ableiten:
* Tatsächliche Aufwandssumme der User Storys pro Sprint W. Aufgrund des CLT ist W normalverteilt, da es die Summe der Aufwände pro User Story ist, und der Aufwand jeder 
einzeln User Story ist zufallsverteilt. Von allen User Storys wird nur ein Anteil fertiggestellt, den wir mit 
  W' bezeichnen wollen.  
* Der Effizienz-Faktor bezeichnet den Faktor, um den die Story-Point-Schätzung vom tatsächlichen Aufwand der User Storys pro Sprint abweicht:
F= Y/X

W' ist ebenfalls normalverteilt. Um jetzt die Parameter von W' schätzen zu können, muss man genügend Sprints absolvieren 
und sich über die o.g. Messgrößen Schätzer für mü und sigma errechnen. Dafür werden aber einige Sprints gebraucht, was einiges 
and Zeit kosten wird. Gibt es einen Weg, um mehr und schneller das systematische Risiko pro Sprint zu lernen? 

Annahmen:
* das Team hat eine unbekannte, aber fixe Größe und daher eine fixe Kapazität, die über die Sprints konstant ist.
* Jeder Sprint besteht aus mehreren User Storys. Für jede US liegt eine Experten-basierte Aufwandsschätzung vor.
* Der wahre Aufwand einer US ist ein Wert, der aus der gleichen Zufallsvariable gezogen wird.
* Das Team wird pro Sprint komplett ausgelastet.

## Bewertung
Das Modell würde prinzipiell gehen, aber man braucht schon einige Sprints, um zu soliden Schätzungen zu kommen. In
der Zwischenzeit mag sich die Projektsituation schon geändert haben.

# Statistisches Modell 2
## Design
W: Tatsächliche Arbeit
S: Schätzung
E: normalverteilter Fehlerterm

W=S+E
## Bewertung
Das Modell würde prinzipiell gehen, aber man braucht schon einige Sprints, um zu soliden Schätzungen zu kommen. In
der Zwischenzeit mag sich die Projektsituation schon geändert haben.

# Risiko-basiertes Modell
## Design
Ich gehe davon aus, dass der Projektleiter und das Projektteam im Rahmen der Sprintplanung bereits die Epics 
identifizieren können, die mit einem hohen Risiko behaftet sind (v.a. technologische, organisatorische 
und Skill-Risiken). Der Eintritt der Risiken ist gewöhnlich mit ungeplantem Aufwand verbunden.
Die Annahme ist daher, dass sich die Liefertreue verbessert, wenn v.a. diese riskanten Epics besonders behandelt und 
gesteuert werden. Ich nehme weiterhin an, dass Epics mit niedrigem Risiko von den Entwicklern im Wesentlichen korrekt 
geschätzt werden können. 

Prinzipien:
* Risikoidentifikation im Rahmen der Sprint-Planung
* Fail Fast, d.h. Epics mit hohem Risiko werden im Sprint mit höchster Priorität angefangen, um den Risikoeintritt frühzeitig
 erkennen zu können.
* Enge Überwachung von riskanten Epics, am besten im Daily. 

Welche Risiken sind v.a. vom Dienstleister verursacht:
* Kapazitätsrisiken
* Skill-Risiken

Welche Risiken sind v.a. vom Auftraggeber verursacht:
* Technologische Risiken, v.a. was die bereitgestellten Tools betrifft.
* Organisatorische Risiken, z.B. fehlende Kapazitäten für Zuleistungen.

Offensichtlich reicht es nicht, den Dienstleister im Vorfeld / während der Sprintplanung auf das erhöhte Risiko 
hinzuweisen. Das für mich am wichtigste Risiko ist das Skill-Risiko - genau das muss ich absichern. Wenn ich 
also von einer Risikoidentifikation rede, dann meine ich eine Einschätzung der Kompetenz, Erfahrung und der technischen 
Expertise des Dienstleisters in Bezug auf das Epic.


## Bewertung


