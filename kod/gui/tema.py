"""Arayüzün renkleri ve yazı tipleri. Tüm ekranlar renkleri buradan alır."""

import customtkinter as ctk

RENKLER = {
    "arka_plan": "#F6F1EA",      # krem sayfa zemini
    "kart": "#FFFFFF",
    "kenar": "#E4DACD",
    "yan_menu": "#2B2118",       # espresso
    "yan_menu_secili": "#43352A",
    "yan_menu_yazi": "#EFE6DA",
    "yan_menu_soluk": "#A8998A",
    "vurgu": "#C8553D",          # terrakota
    "vurgu_koyu": "#A8432F",
    "yazi": "#2B2118",
    "soluk_yazi": "#7A6E63",
    "basari": "#3F7D58",
    "uyari": "#D9A441",
    "uyari_zemin": "#FBF0D9",
    "tehlike": "#B23A48",
    "tehlike_koyu": "#8F2E3A",
    "tablo_baslik": "#EFE6DA",
    "tablo_secili": "#F3D9CF",
    "tablo_cizgi": "#FBF8F4",
}


def yazi(boyut=14, kalin=False):
    """Uygulama genelinde aynı yazı ailesini kullanmak için CTkFont üretir."""
    return ctk.CTkFont(size=boyut, weight="bold" if kalin else "normal")


def temayi_uygula():
    """Uygulama açılırken bir kez çağrılır."""
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
