(* T1 independent symbolic checks for the Myrheim-Meyer ordering fraction. *)

ClearAll[r, d];
r[d_] := Gamma[d + 1] Gamma[d/2]/(2 Gamma[3 d/2]);

report = <|
  "OrderingFractionD2" -> FullSimplify[r[2]],
  "OrderingFractionD4" -> FullSimplify[r[4]],
  "DimensionGrid" -> Table[{dimension, N[r[dimension], 16]}, {dimension, 1, 10}],
  "MonotoneOnIntegerGrid" -> And @@ Thread[Differences[Table[N[r[dimension], 30], {dimension, 1, 10}]] < 0],
  "InverseAtHalf" -> d /. FindRoot[r[d] == 1/2, {d, 2}],
  "RandomnessUsed" -> False
|>;

If[report["OrderingFractionD2"] =!= 1/2, Exit[1]];
If[report["OrderingFractionD4"] =!= 1/10, Exit[1]];

report
