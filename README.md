<div align="center">

# 🖥️ Ryzen 5 5600G + A320M EFI

**EFI configuration repository / Repozytorium konfiguracji EFI**

![Platform](https://img.shields.io/badge/Platform-AMD%20Ryzen-ED1C24?logo=amd&logoColor=white)
![OpenCore](https://img.shields.io/badge/Boot-EFI%20%2F%20OpenCore-555555)

</div>

---

## 🇵🇱 Polski

Repozytorium zawiera katalog **EFI** przygotowany dla konfiguracji opartej na procesorze **AMD Ryzen 5 5600G** i płycie głównej z chipsetem **A320M**, a także katalog `Results` z materiałami związanymi z konfiguracją/testami.

### 📂 Struktura

```text
├── EFI/       # pliki konfiguracji EFI
└── Results/   # rezultaty / materiały pomocnicze
```

### ⚠️ Ważne przed użyciem

Konfiguracje EFI są zależne od konkretnego sprzętu, wersji BIOS/UEFI i używanych komponentów. Nie należy kopiować konfiguracji w ciemno na inny komputer.

Przed zmianami:

1. wykonaj kopię swojej działającej partycji EFI,
2. sprawdź zgodność podzespołów,
3. przejrzyj ustawienia `config.plist`,
4. wygeneruj własne unikalne dane SMBIOS, jeśli konfiguracja ich wymaga,
5. miej przygotowany nośnik umożliwiający przywrócenie poprzedniej konfiguracji.

### 🍎 macOS

Repozytorium nie zawiera instalatora macOS. System operacyjny należy pozyskiwać z oficjalnych źródeł Apple i używać zgodnie z obowiązującymi warunkami licencyjnymi.

### 👤 Repozytorium

Konfiguracja opublikowana i utrzymywana w repozytorium **Swir**.

---

## 🇬🇧 English

This repository contains an **EFI** directory prepared for a configuration based on an **AMD Ryzen 5 5600G** processor and an **A320M** chipset motherboard, together with a `Results` directory containing configuration/testing-related material.

### 📂 Structure

```text
├── EFI/       # EFI configuration files
└── Results/   # results / supporting material
```

### ⚠️ Before using

EFI configurations are hardware-specific and may depend on the exact motherboard, BIOS/UEFI version and installed components. Do not blindly copy this configuration to another machine.

Before making changes:

1. back up your currently working EFI partition,
2. verify hardware compatibility,
3. review the `config.plist` settings,
4. generate your own unique SMBIOS data when required,
5. keep recovery media available so you can restore the previous configuration.

### 🍎 macOS

This repository does not provide a macOS installer. Obtain macOS from official Apple sources and use it in accordance with the applicable license terms.

### 👤 Repository

Configuration published and maintained in the **Swir** repository.
