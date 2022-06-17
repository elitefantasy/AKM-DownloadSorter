; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Akm Download Sorter"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "EliteFantasy"
#define MyAppExeName "AkmDownloadSorter.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{54A2C43B-4D3D-4C3A-9CA6-AB53E29E083D}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={localappdata}\{#MyAppName}
DisableDirPage=yes
DisableProgramGroupPage=yes
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=C:\Users\anilm\Desktop
OutputBaseFilename=AkmDownloadSorter_Setup
SetupIconFile=E:\1 Megasync\my scripts\Github\AKM-DownloadSorter\AKM DownloadSorter\icon\AmazeXsorter.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\{#MyAppExeName}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "E:\1 Megasync\my scripts\Github\AKM-DownloadSorter\AKM DownloadSorter\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\1 Megasync\my scripts\Github\AKM-DownloadSorter\AKM DownloadSorter\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userstartup}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

[code]
const
  SetupMutexName = 'AkmDownloadSorter';

function InitializeSetup(): Boolean;
begin
  Result := True;
  if CheckForMutexes(SetupMutexName) then
  begin
    Log('Mutex exists, setup is running already, silently aborting');
    Result := False;
  end
    else
  begin
    Log('Creating mutex');
    CreateMutex(SetupMutexName);
  end;
end;

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[UninstallRun]
Filename: "{cmd}"; Parameters: "/C ""taskkill /im AkmDownloadSorter.exe /f /t"
