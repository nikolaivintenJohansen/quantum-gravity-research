(* H1 exact audit on the three-element chain, in units rho = 1. *)

bRetarded = {{-2, 0, 0}, {4, -2, 0}, {-8, 4, -2}};
kAction = (bRetarded + Transpose[bRetarded])/2;
field = Array[phi, 3];
action = 1/2 field . bRetarded . field;
gradientResidual = FullSimplify[Grad[action, field] - kAction . field];

report = <|
  "RetardedOperator" -> bRetarded,
  "ActionKernel" -> kAction,
  "RetardedIsSymmetric" -> SymmetricMatrixQ[bRetarded],
  "ActionKernelIsSymmetric" -> SymmetricMatrixQ[kAction],
  "ActionGradientResidual" -> gradientResidual,
  "AdvancedUpperTriangleNormSquared" -> Total[Flatten[UpperTriangularize[kAction, 1]^2]],
  "RandomnessUsed" -> False
|>;

If[gradientResidual =!= {0, 0, 0}, Exit[1]];
report
