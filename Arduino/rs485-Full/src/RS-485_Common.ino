/*
Author:     Loreto Notarantonio
version:    LnVer_2017-07-26_09.22.27

Scope:      Funzioni comuni

*/


// ################################################################
// # - Copia l'intero messaggio
// # -  RxBuffer --> TxBuffer
// ################################################################
void copyRxMessageToTx(RXTX_DATA *pData) {
        // - copy ALL rx to tx
    for (byte i = 0; i<=pData->rx[DATALEN]; i++)
        pData->tx[i] = pData->rx[i];         // copiamo i dati nel buffer da inviare
}


// const char INO_RX[] = "RX-ino";
// const char INO_Prefix[] = "TX-ino";
// #############################################################
// # Inserisce nella risposta un messaggio (di errore o altro)
// #############################################################
void prepareMessage(RXTX_DATA *pData, byte cmdData[], byte dataLen) {
    // displayMyData(INO_Prefix,  LN_OK, pData);
    copyRxMessageToTx(pData); // ci portiamo anche il numero messaggio...
    // displayMyData(INO_Prefix,  LN_OK, pData);


    byte index = COMMAND_DATA-1;
    for (byte i=0; (i<dataLen) && (i<MAX_DATA_SIZE); i++)
        pData->tx[++index] = cmdData[i];         // copiamo i dati nel buffer da inviare


    pData->tx[DATALEN] = --index;  // update dataLen
    // displayMyData(INO_Prefix,  LN_OK, pData);
}





