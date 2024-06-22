{
  description = "basic Python 3.10 environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-23.05";
  };


  outputs = { self, nixpkgs }:
    let
      # The set of systems to provide outputs for
      allSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      # A function that provides a system-specific Nixpkgs for the desired systems
      # Construct function 'forAllSystems' that takes a function 'f' and is called 
      # with aargument'system' for with each value defined in 'allSystems' array.
      # the 'genAttrs' function takes an array and a function that defines pkgs
      forAllSystems = f: nixpkgs.lib.genAttrs allSystems (system: f {
        # pkgs = import nixpkgs { inherit system; };
        pkgs = nixpkgs.legacyPackages.${system};
      });
    in
    {
      # pkgs is a function takes takes 'system' to know which platform 
      # it should build for, as not provided it is 'curried' with a 'system'
      # input argument. 'forAllSystems' when calls the pkgs curry for each
      # value
      devShells = forAllSystems ({ pkgs }: {
        default =
          pkgs.mkShell {
            buildInputs = [
              pkgs.python310
            ];

            shellHook = ''
             # escaped $ with double tick such that ''$
             # see: https://nixos.org/manual/nix/stable/language/values.html
             export PS1='\n\e[1;34m($CONSOLES)\e[0m \e[1;37m''${PWD#"''${PWD%/*/*}/"}\e[0m \e[38;2;195;217;247m\D{%y-%m-%d %H:%M:%S}\e[0m  \n\001\e[38;2;14;169;236m\]$\[\e[0m\002 ' 

              # don't create files in my $HOME, keep all here
              # export HOME=$PWD/.nix_local;

              # ensure yarn workspaces foreach commands output color
              export FORCE_COLOR=true

              VIRTUAL_ENV="''${1:-.venv}";

              (
              set -euo pipefail
              # -e: exit on error
              # -u: treat unset variables as errors
              # -o pipefail: exit if any command pipe has a failure
              
              # create virtual environment and activate
              if [ ! -f "''$VIRTUAL_ENV/bin/activate" ]; then
                echo "''$VIRTUAL_ENV does not exist. Creating ''$VIRTUAL_ENV and activating virtual environment."
                python -m venv "''$VIRTUAL_ENV"
              fi
              )
              
              source "''$VIRTUAL_ENV/bin/activate"


#             # source ./scripts/load-dotenv.sh
#             # ensure pip is present, and is up-to-date
#             python -m ensurepip --upgrade
#             pip install --upgrade pip
            '';

            CONSOLES = "nix";
          };
      });
    };
}

