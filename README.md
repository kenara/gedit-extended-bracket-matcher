# Extended Bracket Matcher for Gedit

This Gedit plugin extends the built-in bracket matching feature to work with **very large code blocks**.

Normally, Gedit displays a “Bracket match is out of range” error when the matching bracket is more than ~2000 characters away. This plugin removes that limitation by scanning a much larger range and reporting the matching bracket’s **line number** in the status bar.

---

## 🔍 Features

- Detects matching brackets: `()`, `{}`, `[]`
- Handles blocks of code thousands of lines long
- Works when the cursor is placed **next to** a bracket (either side)
- Displays the **matching line number** in the Gedit status bar
- Silent and seamless — no UI clutter or config required

---

## 🧑‍💻 Installation

1. Clone or download this repository:

```bash
git clone https://github.com/kenara/gedit-extended-bracket-matcher.git
```

2. Copy the plugin folder to your local Gedit plugins directory:

```bash
mkdir -p ~/.local/share/gedit/plugins
cp -r gedit-extended-bracket-matcher ~/.local/share/gedit/plugins/extendedbrackets
```

3. Launch Gedit and enable the plugin:

- Go to `Edit` → `Preferences` → `Plugins`
- Check **Extended Bracket Matcher**

---

## 📝 License

This plugin is licensed under the [MIT License](LICENSE).
