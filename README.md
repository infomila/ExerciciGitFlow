# TaskFlow

A tiny command-line task manager used as the practice repository for the
Git / GitFlow workshop. The code itself is intentionally small — the point
of this project is the *history*, not the app.

Tasks are stored in memory only (no persistence between runs); that's
deliberate, so don't be surprised when `taskflow list` comes back empty in a
new process.

## Running it

    python -m taskflow.cli add "Prepare workshop slides"
    python -m taskflow.cli list

## Running the tests

    python -m unittest discover

## The exercise

See [EXERCICI.md](EXERCICI.md) for the workshop instructions. Start there.
