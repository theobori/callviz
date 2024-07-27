{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      forEachSupportedSystem =
        f: nixpkgs.lib.genAttrs supportedSystems (system: f { pkgs = import nixpkgs { inherit system; }; });
    in
    {
      packages = forEachSupportedSystem (
        { pkgs }:
        {
          default = pkgs.callPackage ./. {
            inherit (pkgs.python311.pkgs)
              buildPythonPackage
              setuptools
              wheel
              graphviz
              ;
          };
        }
      );

      devShells = forEachSupportedSystem (
        { pkgs }:
        {
          default = pkgs.mkShell {
            venvDir = ".venv";
            packages =
              with pkgs;
              [ python311 ]
              ++ (with pkgs.python311Packages; [
                pip
                venvShellHook
                graphviz
              ]);
          };
        }
      );
    };
}
