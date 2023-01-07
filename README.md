# PyTexGost

Project for automatic generation of programm text document with state standard (ГОСТ) using latex and python.

## Troubleshooting
- In windows OS. **"Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?"**.
  - Check what docker enabled at docker-desktop settings ("Enable integration with my default WSL distro"); 
  - Use another shell (for example `just --shell=powershell start`)