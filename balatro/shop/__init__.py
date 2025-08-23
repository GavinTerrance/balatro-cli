"""Shop-related modules and utilities.

The package exports lightweight components that are safe to import
without triggering expensive or circular dependencies.  The `Shop`
class itself performs imports from the cards package, so it is
*not* re-exported here to avoid circular imports during module
initialisation.
"""

from .vouchers import Voucher
from .stickers import Sticker, StickerType

__all__ = ["Voucher", "Sticker", "StickerType"]
