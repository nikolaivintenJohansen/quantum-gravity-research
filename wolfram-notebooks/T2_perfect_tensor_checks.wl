(* T2 exact stabilizer-algebra cross-check in Wolfram Language. *)

id = IdentityMatrix[2];
x = {{0, 1}, {1, 0}};
z = {{1, 0}, {0, -1}};
pauli = <|"I" -> id, "X" -> x, "Z" -> z|>;
op[string_] := KroneckerProduct @@ (pauli /@ Characters[string]);

generators = op /@ {"XZZXI", "IXZZX", "XIXZZ", "ZXIXZ"};
logicalZ = op["ZZZZZ"];
codeProjector = Fold[#1 . ((IdentityMatrix[32] + #2)/2) &, IdentityMatrix[32], generators];
logicalZeroProjector = codeProjector . ((IdentityMatrix[32] + logicalZ)/2);

report = <|
  "GeneratorsSquareToIdentity" -> And @@ ((Max[Abs[Flatten[# . # - IdentityMatrix[32]]]] == 0) & /@ generators),
  "GeneratorsMutuallyCommute" -> And @@ Flatten[Table[Max[Abs[Flatten[generators[[i]] . generators[[j]] - generators[[j]] . generators[[i]]]]] == 0, {i, 4}, {j, 4}]],
  "CodeProjectorRank" -> MatrixRank[codeProjector],
  "LogicalZeroProjectorRank" -> MatrixRank[logicalZeroProjector],
  "RandomnessUsed" -> False
|>;

If[report["CodeProjectorRank"] =!= 2, Exit[1]];
If[report["LogicalZeroProjectorRank"] =!= 1, Exit[1]];

report
