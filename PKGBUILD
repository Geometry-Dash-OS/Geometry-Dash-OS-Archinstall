pkgname=gd-archinstall
pkgver=1.0.0
pkgrel=1
pkgdesc="Just another guided/automated Arch Linux installer with a twist"
arch=(any)
url="https://github.com/Geometry-Dash-OS/Geometry-Dash-OS-Archinstall"
license=(GPL3)
depends=(
  'arch-install-scripts'
  'btrfs-progs'
  'coreutils'
  'cryptsetup'
  'dosfstools'
  'e2fsprogs'
  'glibc'
  'kbd'
  'pciutils'
  'procps-ng'
  'python'
  'python-pyparted'
  'python-simple-term-menu'
  'systemd'
  'util-linux'
)
makedepends=(
  'python-setuptools'
  'python-sphinx'
  'python-build'
  'python-installer'
  'python-wheel'
)
optdepends=(
  'python-systemd: Adds journald logging'
)
source=(
  $pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz
)

pkgver() {
  cd $pkgname-$pkgver

  awk '$1 ~ /^__version__/ {gsub("\"", ""); print $3}' archinstall/__init__.py
}

prepare() {
  cd $pkgname-$pkgver

  # use real directories for examples and profiles, as symlinks do not work
  rm -fv $pkgname/{examples,profiles}
}

build() {
  cd $pkgname-$pkgver

  python -m build --wheel --no-isolation
  PYTHONDONTWRITEBYTECODE=1 make man -C docs
}

package() {
  cd "$pkgname-$pkgver"

  python -m installer --destdir="$pkgdir" dist/*.whl
  install -vDm 644 docs/_build/man/archinstall.1 -t "$pkgdir/usr/share/man/man1/"
}
