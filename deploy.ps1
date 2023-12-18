# PowerShell script to copy files to a remote host using scp

# Define local and remote directories
$localDirectory = "C:\path\to\local\directory\*"
$remoteUser = "pi"
$remoteHost = "pi"
$remoteDirectory = "/home/pi/Desktop/GMU/"

# Ensure the OpenSSH client is installed
if (-not (Get-Command "scp" -ErrorAction SilentlyContinue)) {
    Write-Error "SCP command not found. Please ensure OpenSSH client is installed."
    exit 1
}

# Copy files using scp
# Note: PowerShell does not support password authentication for SCP natively.
# You would need to set up SSH keys for passwordless authentication.
# If SSH keys are not set up, you will be prompted for a password.
$scpCommand = "scp -r $localDirectory $remoteUser@$remoteHost:$remoteDirectory"
Invoke-Expression $scpCommand

# If you need to specify a different SSH port or a path to a private key, you can add the appropriate scp options:
# $scpCommand = "scp -i C:\path\to\private\key -P 2222 -r $localDirectory $remoteUser@$remoteHost:$remoteDirectory"
# Invoke-Expression $scpCommand
