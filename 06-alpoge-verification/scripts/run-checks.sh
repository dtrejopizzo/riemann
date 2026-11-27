#!/bin/bash
# Run as user `lean` in ~/lean after `lake build` has completed.
cd ~/lean && ulimit -n 1048576
lake env lean AxiomCheck.lean      > ~/axioms.log 2>&1
lake env lean Step5Statement.lean  > ~/step5-statement.log 2>&1
lake env lean Step5Extract.lean    > ~/step5-extract.log 2>&1
