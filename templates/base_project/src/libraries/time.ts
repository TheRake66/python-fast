export type ParsedTime = {
  hours: number;
  minutes: number;
  seconds: number;
}

export function parseTime(time: number): ParsedTime {
  const total = Math.floor(time);
  const hours = Math.floor(total / 3600);
  const minutes = Math.floor((total % 3600) / 60);
  const seconds = total % 60;
  return { hours, minutes, seconds };
}

export function formatTime(time: ParsedTime): string;
export function formatTime(seconds: number): string;
export function formatTime(value: ParsedTime | number): string {
  const time = typeof value === 'number' ? parseTime(value) : value;
  const pad = (value: number): string => value.toString().padStart(2, '0');
  return `${pad(time.hours)}:${pad(time.minutes)}:${pad(time.seconds)}`;
}