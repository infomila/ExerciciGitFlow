# Repte de Git i GitFlow — TaskFlow

Benvinguts! Aquest repositori és un entorn de proves per practicar
Git i el model de ramificació GitFlow. Tot aquest exercici és **local**: sense
`git push`, sense remots, sense GitHub. Només tu, `git` a la línia d'ordres i
aquest repositori.

El codi és un gestor de tasques minúscul escrit en Python. No cal que sàpigues
gaire Python per fer aquest exercici: el codi és senzill a propòsit, perquè el
que importa és l'*historial*, no l'aplicació. Quan et sigui útil, executa les
proves (`python -m unittest discover`) per comprovar que una fusió (`merge`) o
un `rebase` no ha trencat res.

## Model de ramificació

Aquest repositori segueix GitFlow:

- `main` — sempre a punt per a producció. Només avança mitjançant una branca
  `release/*` o `hotfix/*` finalitzada. Cada commit de `main` està etiquetat
  (*tag*).
- `develop` — la branca d'integració. Les funcionalitats acabades hi arriben
  primer.
- `feature/*` — una branca per funcionalitat, creada a partir de `develop` i
  fusionada de nou a `develop` quan està acabada.
- `release/*` — es crea a partir de `develop` quan prepares una versió per
  publicar. Aquí només es fan els últims retocs i correccions. Es finalitza
  fusionant-la a **les dues** branques: `main` (amb etiqueta) i `develop`.
- `hotfix/*` — es crea a partir de `main` per corregir un error crític en
  producció sense arrossegar feina inacabada de `develop`. Es finalitza
  fusionant-la a **les dues** branques: `main` (amb etiqueta) i `develop`.

## Abans de començar

Fes una ullada al repositori abans de tocar res:

```
# git log --all --graph --oneline --decorate
git lg1 # la nostra versió tunejada de git log 
git branch -a
git show v0.1.0
```

Observa que:
- `main` té dos commits i una etiqueta, `v0.1.0`.
- `develop` parteix de `main` i té els seus propis commits, entre els quals hi
  ha un commit de fusió (la branca `feature/add-task-cli` ja te l'hem deixada
  acabada: és un exemple de com queda una funcionalitat ben finalitzada i
  integrada).
- Hi ha tres branques de funcionalitat esperant-te: `feature/list-tasks`,
  `feature/delete-task` i `feature/notifications`. Cap d'elles no s'ha
  fusionat encara.

Llegeix les diferències de cada branca de funcionalitat respecte de `develop`
abans de fusionar res:

```
git diff develop...feature/list-tasks
git diff develop...feature/delete-task
git log develop..feature/notifications --oneline
```

---

## Part A — Branques, commits i les teves primeres fusions

### Pas 1 — Crea una branca i fes-hi un commit

Crea la branca `feature/task-priority` a partir de `develop`. Afegeix un camp
`priority` a la classe `Task` de `taskflow/tasks.py` (una cadena de text amb el
valor per defecte `"normal"`; insereix-lo **entre `title` i `done`** perquè els
passos posteriors encaixin sense problemes). Fes-ne un commit amb un missatge
que descrigui el canvi.

### Pas 2 — Fusiona-la a `develop`

Fusiona `feature/task-priority` a `develop`. Fes servir `--no-ff`: a GitFlow,
les fusions de funcionalitats sempre creen un commit de fusió, fins i tot quan
Git pot fer un *fast-forward*, perquè l'historial mostri que la funcionalitat
ha existit com a línia de treball pròpia. Compara la sortida de
`git lg1` abans i després i fixa't en la diferència que fa un commit de
fusió.

### Pas 3 — Una fusió de funcionalitat sense conflictes

Fusiona `feature/list-tasks` a `develop` (`--no-ff`). S'hauria d'aplicar sense
conflictes. Executa les proves després de fer-ho.

### Pas 4 — Una fusió de funcionalitat amb conflicte

Fusiona `feature/delete-task` a `develop` (`--no-ff`). Aquesta fusió **donarà**
conflicte: les dues branques han editat `taskflow/cli.py` de manera
independent.

- Executa `git status` per veure quins fitxers tenen conflicte.
- Obre el fitxer: hi trobaràs **tres** blocs separats amb els marcadors
  `<<<<<<<`, `=======` i `>>>>>>>` (Git no ha sabut veure que dues insercions
  properes no tenen res a veure l'una amb l'altra). Repassa'ls un per un.
- Resol-los de manera que es conservi el comportament de totes dues
  funcionalitats (no esborris simplement un dels dos costats). Per a la
  descripció del parser, combina les dues cadenes en una de sola; als altres
  dos blocs, conserva tant la part de `list` com la de `delete`.
- Fes `git add` dels fitxers resolts i completa la fusió.
- Comprova-ho executant `python -m unittest discover` i rellegint les funcions
  `build_parser()` i `main()` ja fusionades, per assegurar-te que no s'ha perdut
  res sense voler.

---

## Part B — Preparar una release i un hotfix

### Pas 5 — Finalitzar una release a l'estil GitFlow

1. Crea `release/0.2.0` a partir de `develop`.
2. A la branca de release: actualitza `__version__` a `"0.2.0"` dins de
   `taskflow/__init__.py` i afegeix una secció `## [0.2.0]` a `CHANGELOG.md`
   que resumeixi què hi ha de nou. Fes-ne un commit.
3. «Finalitza» la release:
   - Canvia a `main`, fusiona-hi `release/0.2.0` amb `--no-ff` i etiqueta el
     resultat com a `v0.2.0`.
   - Canvia a `develop` i fusiona-hi també `release/0.2.0` amb `--no-ff`: els
     commits de la release han d'arribar a totes dues branques.
4. Esborra `release/0.2.0` quan les dues fusions estiguin fetes.

### Pas 6 — Finalitzar un hotfix

Arriba un informe d'error: `taskflow add ""` (un títol buit) peta en lloc de
fallar de manera controlada.

1. Crea `hotfix/0.2.1` a partir de `main` (**no** de `develop`: un hotfix
   corregeix el que realment hi ha en producció).
2. Arregla'l: a `taskflow/cli.py`, fes que l'ordre `add` rebutgi un títol en
   blanc (o només amb espais) amb un error clar, en lloc de deixar-lo passar.
   Ja que hi ets, a `taskflow/tasks.py` afegeix també un comentari curt en línia
   al camp `done` que expliqui què significa.
3. Finalitza el hotfix: fusiona'l a `main` amb `--no-ff`, etiqueta el resultat
   com a `v0.2.1` i porta també la correcció a `develop`.
4. *Opcional:* en lloc de fusionar a `develop` al punt 3, prova
   `git cherry-pick <commit>` en una branca temporal i compara el resultat.
   Quan podries preferir un cherry-pick a una fusió en aquest cas?

---

## Part C — Fer rebase

`feature/notifications` porta aturada des d'abans de la release i del hotfix. A
més, té un historial de commits desordenat: sis commits, entre els quals
«wip», «fix typo» i «more wip». Toca resoldre tots dos problemes.

### Pas 7 — Rebase sobre el `develop` que ha avançat (hi haurà un conflicte)

```
git switch feature/notifications
git rebase develop
```

Com que `develop` ha avançat (ara inclou la release i el hotfix), això reaplica
els sis commits de `feature/notifications` a sobre de la nova punta, i un
d'ells toca la mateixa línia de `taskflow/tasks.py` que va tocar el hotfix. Git
s'aturarà a mig camí amb un conflicte.

- `git status` t'indicarà quin commit s'està reaplicant i què té conflicte.
- Resol el conflicte a `taskflow/tasks.py` (conserva tant el comentari del
  hotfix com el nou camp `remind_at`), fes `git add` del fitxer i executa
  `git rebase --continue`.
- La resta de commits s'haurien de reaplicar sense problemes. Si alguna cosa va
  malament, `git rebase --abort` et retorna al punt de partida: pots
  abandonar-ho i tornar-ho a provar sense cap risc.

### Pas 8 — Fes servir el rebase per reduir l'historial

Sis commits, incloent-hi dos de tipus «wip» i una correcció tipogràfica, no és
el que voldries que veiessin els altres en llegir `git log`. Neteja l'historial:

```
git rebase -i develop
```

A l'editor interactiu, fes servir `squash` o `fixup` per reduir els sis commits
a un o dos commits amb missatges clars i significatius (per exemple:
«Add due-date reminders to tasks»). Reformula'ls amb `reword` si cal.

### Pas 9 — Fusiona la funcionalitat ja endreçada

Fusiona `feature/notifications` a `develop`. Observa que s'aplica a l'instant:
com que al Pas 7 vas fer el rebase sobre la punta actual de `develop`, ja no
queda res per reconciliar. Fes servir `--no-ff` igualment, per coherència amb
la resta de fusions de funcionalitats d'aquest repositori. Després, esborra la
branca de la funcionalitat.

---

## Part D — Cloenda

### Pas 10 — Llegeix el resultat

```
git log --all --graph --oneline --decorate
```

Compara'l amb el diagrama de l'article «A successful Git branching model»
(nvie.com). Hauries de veure: `main` avançant només en els punts de
release/hotfix etiquetats, `develop` com a fil conductor i les branques de
funcionalitat com a bombolles de fusió al llarg del recorregut.

### Reflexió

Respon aquestes preguntes en unes poques frases cadascuna (en un fitxer de
text, o simplement prepara't per comentar-les):

1. On has triat fer un `merge` i on has triat fer un `rebase`? Què hauria anat
   malament si haguessis intercanviat les dues opcions?
2. Per què GitFlow fusiona una release o un hotfix finalitzats a **les dues**
   branques, `main` i `develop`, en lloc de fer-ho només a una?
3. `git rebase` reescriu els commits (nous SHA). Per què això és segur a
   `feature/notifications` en aquest cas, però s'ha de fer amb cura en una
   branca en què també treballen altres persones? (Això importa més quan hi ha
   remots pel mig: un tast de l'exercici següent.)

## Extres (opcional, prova-ho en branques temporals)


- **Reordenar commits:** en un rebase interactiu, reordena dos commits en lloc
  de fer-ne un squash, i pensa en quins casos Git et deixarà fer-ho sense
  conflicte i en quins no.

