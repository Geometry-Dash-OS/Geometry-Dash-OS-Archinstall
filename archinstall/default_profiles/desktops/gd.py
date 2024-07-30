from typing import List, Optional, Any, TYPE_CHECKING

from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

if TYPE_CHECKING:
	_: Any


class GDProfile(XorgProfile):
	def __init__(self):
		super().__init__('GD', ProfileType.DesktopEnv, description='')

	@property
	def packages(self) -> List[str]:
		return [
			"geometry-dash-wm",
			"geometry-dash-plymouth-theme"
		]

	@property
	def default_greeter_type(self) -> Optional[GreeterType]:
		return GreeterType.Gdm
