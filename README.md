### Instlling Shell Configuration

Install Oh My Zsh   
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```   

Install Antigen   
```
curl -L git.io/antigen > antigen.zsh
```   

cd into home directory   
```
cd $HOME
```   
Create github directory (optional but recommended. I make this to organize any repos I might clone)   
```
mkdir github
```   
Clone this repo   
```
git clone https://github.com/LovecraftianGodsKiller/RandomStuff.git
```   
cd into cloned repo   
```
cd RandomStuff
```   
Backup and copy .zshrc   
```
mv ~/.zshrc ~/.zshrc.bak && cp ./dotfile/.zshrc ~/
```   
Backup and copy .p10k.zsh   
```
mv ~/.p10k.zsh ~/.p10k.zsh.bak && cp./dotfile/.p10k.zsh ~/
```  
Restart zsh   
```
exec zsh
```   

### Installing Package Configuration   

Neofetch   
```
cp ./dotconfig/neofetch/* ~/.config/neofetch/
```   

lsd   
```
cp -r ./dotconfig/lsd/* ~/.config/lsd/
```   

kitty   
```
cp ./dotconfig/kitty/* ~/.config/kitty/
```   

Arch Linux
   

From Pacman   
  exa   
  alacritty   
  btop   
  flameshot   
  jdk-openjdk   
  discord   
  kvantum   
  micro   
  qbittorrent   
  steam   
  wine-staging   
Pacman (not remebering if preinstalled)   
  neofetch   
  python
   
   
From AUR   
  firefox-developer-edition   
  github-desktop-bin   
  heroic-games-launcher-bin   
  input-remapper-git   
  prismlauncher-qt5   
  spotify   
  xclicker   
   

From PyPI   
  konsave - python -m pip install konsave   
   
   
From Flatpak   
  [Bottles](https://flathub.org/apps/details/com.usebottles.bottles)   
  [Obsidian](https://flathub.org/apps/details/md.obsidian.Obsidian)   
   
   
AppImages   
  [BetterDiscord](https://betterdiscord.app/)   
   
   
Obisidian Plungins and themes   
  Plugins   
    Advanced Tables   
    Dataview   
    Editor Syntax Highlight   
    Linter   
    Style Settings   
    Templater   
  Theme(s)   
    Prism   
      Appearance   
        Dark Theme   
          Color Scheme   
            Indigo   
          Accent Style   
            Border and Filled   
          Accent Color Preset   
            Purple   
          Accent Text Color Preset   
            Accent Color   
      Editor   
   

Others   
  [klassy](https://github.com/paulmcauley/klassy)   
  [oh-my-zsh](https://ohmyz.sh/)   
  [spicetify](https://spicetify.app/)   
   

KDE Appearance   
  Application Style - kvantum   
  Plasma Style - Breeze   
  Colors - Dracula-purple   
  Window Decorations - Klassy   
  Font Size - 8pt   
  Icons - Papirus Colors Dark   
  Cursors - Breeze   
   

Kvantum   
  Theme - Dracula-purple   
  Translucent Windows   
  	Reduce window opacity by - 15%   
  	Reduce Menu Opacity by - 90%   
   

oh-my-zsh plugins   
  [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md)   
  [zsh-history-substring-search](https://github.com/zsh-users/zsh-history-substring-search)   
  [archlinux (pacman and aur helper quick commands)](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/archlinux)   
  [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md)   
