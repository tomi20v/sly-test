# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"
  # Use https://search.nixos.org/packages to find packages
  packages = [ pkgs.python3 pkgs.mariadb pkgs.nodejs_20 ];
  services.mysql = {
    enable = true;
    package = pkgs.mariadb;
    #ensureDatabases = [ "emry" ];
  };
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      "ms-python.python"
      "rangav.vscode-thunder-client"
      "mtxr.sqltools"
      "mtxr.sqltools-driver-mysql"
      "vue.volar"
    ];
    workspace = {
      # Runs when a workspace is first created with this `dev.nix` file
      onCreate = {
        install =
          "cd backend && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
        init-db = "mysql -u root < init.sql";
        npm-install = "npm ci --no-audit --prefer-offline --no-progress --timing";
        # Open editors for the following files by default, if they exist:
        default.openFiles = [ "README.md" "src/index.html" "main.py" ];
      };
      # Runs when a workspace is (re)started
      onStart = {
        run-server = "cd backend && ./devserver.sh";
      };
    };
    previews = {
      enable = true;
      previews = {
        web = {
          command = ["npm" "run" "dev" "--" "--port" "$PORT" "--host" "0.0.0.0"];
          manager = "web";
          cwd = "frontend";
        };
      };
    };
  };
}

