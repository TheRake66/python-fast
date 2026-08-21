import configuration from '../configuration.json';

const defaultState = configuration.default.fullscreen;
const storageKey = configuration.localstorage.fullscreen;

export function initFullscreen(): void {
  const fullscreen = localStorage.getItem(storageKey) ?? defaultState;
  if (fullscreen && !isFullscreen()) {
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
  localStorage.setItem(storageKey, '');
}

export function exitFullscreen(): void {
  if (isFullscreen()) 
    document.exitFullscreen();
  localStorage.removeItem(storageKey)
}

export function isFullscreen(): boolean {
  return document.fullscreenElement !== null
}