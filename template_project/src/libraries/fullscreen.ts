import Cookies from 'js-cookie';

export function initFullscreen(): void {
  const fullscreen = Cookies.get('fullscreen');
  if (fullscreen !== undefined && !isFullscreen()) {
    const handler = () => {
      requestFullscreen();
      window.removeEventListener('click', handler);
    };
    window.addEventListener('click', handler);
  }
}

export function requestFullscreen(): void {
  if (!isFullscreen())
    document.documentElement.requestFullscreen();
  Cookies.set('fullscreen', '');
}

export function exitFullscreen(): void {
  if (isFullscreen()) 
    document.exitFullscreen();
  Cookies.remove('fullscreen')
}

export function isFullscreen(): boolean {
  return document.fullscreenElement !== null
}