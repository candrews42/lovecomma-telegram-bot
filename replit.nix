{pkgs}: {
  deps = [
    pkgs.ffmpeg-full
    pkgs.inetutils
    pkgs.rustc
    pkgs.libiconv
    pkgs.cargo
  ];
}
