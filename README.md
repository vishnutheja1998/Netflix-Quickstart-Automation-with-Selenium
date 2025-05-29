# Netflix Quickstart Automation with Selenium

This project automates the following actions on Netflix using Python and Selenium:

1. Launches Chrome using your own Chrome profile
2. Skips login (since you’re already signed in)
3. Selects the **“Sravya”** profile (if prompted)
4. Searches for the movie **"The Wild Robot"**
5. Clicks the movie to open the preview
6. Clicks the **Resume** or **Play** button
7. Enters fullscreen mode by clicking the player fullscreen button

> ✅ Built and tested on macOS ✅ Python 3.9+ ✅ Chrome 136+

---

## 🔧 Setup

1. **Install Python & Pip**

   ```bash
   python3 --version
   ```

2. **Install Selenium**

   ```bash
   pip3 install selenium
   ```

3. **Install ChromeDriver**

   ```bash
   brew install chromedriver
   ```

4. **Configure Profile Path**
   In `netflix_quickstart.py`, replace:

   ```python
   chrome_options.add_argument(
     "--user-data-dir=/Users/YOUR_USERNAME/selenium-profile"
   )
   ```

   with your actual macOS username.
   Find your profile via `chrome://version/` → **Profile Path**.

---

## ▶️ Usage

```bash
python3 netflix_quickstart.py
```

> * Ensure Chrome is closed if you’re using your default profile.
> * On first run with a new Selenium profile you’ll need to sign into Netflix manually.

---

## ⚠️ Notes

* **Personal & educational use** only.
* Netflix may change its UI, which can break selectors.
* Fullscreen relies on clicking the in-player control.

---

## 📄 License

MIT License
