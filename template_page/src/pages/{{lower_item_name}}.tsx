import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import styles from './{{lower_item_name}}.module.scss';

export default function {{capitalize_item_name}}() {
  const { t } = useTranslation('', { keyPrefix: 'components.{{lower_item_name}}' });
  
  return (
    <main className={styles.container}>
      Bonjour la page {{capitalize_item_name}} !
    </main>
  );
}