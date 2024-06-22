{
  lib,
  buildPythonPackage,
  setuptools,
  wheel,
  graphviz,
}:
buildPythonPackage rec {
  pname = "callviz";
  version = "0.2.0";
  pyproject = true;

  src = ./.;

  nativeBuildInputs = [
    setuptools
    wheel
  ];

  propagatedBuildInputs = [ graphviz ];

  meta = {
    changelog = "https://github.com/theobori/callviz/releases/tag/v${version}";
    description = "It is a Python decorator that will help you visualizate the function calls, in particular for the recursive ones.";
    homepage = "https://github.com/theobori/callviz";
    license = lib.licenses.mit;
  };
}
